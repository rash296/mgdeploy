from django.shortcuts import render
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QueryForm
from django.core.mail import send_mail
from django.conf import settings


from chartit import DataPool, Chart
import simplejson


from .models import Document,TestRecord, Test,Attendance, AttendanceRecord,MonthlyWeatherByCity,StudentSheet, ParentSheet, Schedules,News
from .forms import DocumentForm, TestForm, AttendanceForm, QueryForm, notifyForm, RegistrationForm,StudentForm,ParentForm


# Create your views here.

from django.contrib.auth.models import User, Group
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login




@csrf_protect
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
				)
			return HttpResponseRedirect('/register/success/')

	else:
		form = RegistrationForm()

	variables = RequestContext(request, {'form': form})

	return render_to_response('registration/register.html',variables,)
 
def register_success(request):
	return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def loginhome(request):
	#user = User.objects.create_user(username='131001.P',password='131001')
	#user.groups.add(Group.objects.get(name='Parent'))
	return render_to_response('loginhome.html',{ 'user': request.user })





def user(request):
	#is_student = request.user.groups.filter(name='Student').exists()

	users_in_group=Group.objects.get(name="Student").user_set.all()
	user=request.user

	if user in users_in_group:
		is_student=True
	else:
		is_student=False	

		
	context = {'user': user,
				'groups': user.groups.all(),
				'is_student':is_student
				}

	return render_to_response('loginhome.html', context,context_instance=RequestContext(request))

def announcements(request):
	schedule=Schedules.objects.all().order_by('date')
	#testset=TestRecord.objects.all()
	#max_test=TestRecord.objects.aggregate(Max('test_no'))
	max_test=TestRecord.objects.all().order_by('-test_no')[0]
	number=max_test.test_no
	top_ten=TestRecord.objects.all().filter(test_no=number).order_by('-stud_score')
	news=News.objects.all().order_by('message_ID')

	context={
		'schedule':schedule,
		'max_test':max_test,
		'top_ten':top_ten,
		'news':news,

	}
	return render(request,'announcement.html',context)


def query(request):
	form=QueryForm(request.POST or None)
	if form.is_valid():
		form_email=form.cleaned_data.get("Your_email")
		form_message=form.cleaned_data.get("Your_query")
		subject='Parent Query'
		print(form_email)
		from_email=form_email
		#settings.EMAIL_HOST_USER is defined in settings.py
		to_email=[settings.EMAIL_HOST_USER,'mallipeddiakshay@gmail.com']
		query_message="%s has sent a query: %s"%(
				form_email,
				form_message)
		
       
        		
        		
		send_mail(subject,
			query_message,
			from_email,
			to_email,
			fail_silently=False)



		
	context={
        "form":form,


	}
	return render(request,"forms.html",context)


def notify(request):
	form=notifyForm(request.POST or None)
	if form.is_valid():
		notification_message=form.cleaned_data.get("Notification_message")
		subject='Notification from M.G coaching insititute'
		#settings.EMAIL_HOST_USER is defined in settings.py

		from_email=settings.EMAIL_HOST_USER

		to_email=['rashmiwilson296@gmail.com','mallipeddiakshay@gmail.com']
       
        		
        		
		send_mail(subject,
			notification_message,
			from_email,
			to_email,
			fail_silently=False)



		
	context={
        "form":form,


	}
	return render(request,"notify.html",context)	


def profile(request):
	if request.user.groups.filter(name='Student').exists():
		stud_ID=request.user.get_username()
		

	elif request.user.groups.filter(name='Parent').exists():
		line=request.user.get_username().split('.')
		stud_ID=line[0]
		
	else:
		stud_ID=131001

		
	testset=TestRecord.objects.all().filter(stud_ID=stud_ID).order_by('test_no')
	attset=AttendanceRecord.objects.all().filter(stud_ID=stud_ID)

	count=0
	total=0
	

	for i in attset:
		total=total+1
		print total
		if i.stud_presence==1:
			count=count+1

			
	testdata = \
		DataPool(
			series=
			[{'options': {
				'source': TestRecord.objects.all().filter(stud_ID=stud_ID)},
				'terms': [
					'test_no',
					'stud_score',
					'test_avg']}
					])

    #Step 2: Create the Chart object
	cht = Chart(
			datasource = testdata,
			series_options =
			[{'options':{
				'type': 'line',
				'stacking': False},
				'terms':{
					'test_no': [
					'stud_score',
					'test_avg']
					}}],
			chart_options =
				{'title': {
					'text': ''},
				'xAxis': {
					'title': {
						'text': 'Test number'}}})
		
	context={
		"testset": testset,
		'user':request.user,
		"stud_ID":stud_ID,
		'chart': cht,
		'total':total,
		'count':count,
		#"count": count,
	}
	return render_to_response('profile.html',context)


def home(request):
	
	return render(request,'home.html',{})


def about(request):
	return render(request,'about.html',{})

def base(request):
	return render(request,'base.html',{})	

def contact(request):
	return render(request,'contact.html',{})

def achievement(request):
	return render(request,'achievement.html',{})


def list(request):
	if request.method=='POST':
		form=DocumentForm(request.POST, request.FILES)
		if form.is_valid() :
			newdoc=Document(docfile=request.FILES['docfile'])
			newdoc.save()

			return HttpResponseRedirect(reverse('webapp.views.list'))

		
	else :
		form=DocumentForm()

	documents=Document.objects.all()
	
	return render_to_response(
		'list.html',
		{'documents':documents, 
			'form':form},
		context_instance=RequestContext(request))


def test(request):
    # Handle file upload
	if request.method == 'POST':
		form = TestForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Test(testsheet = request.FILES['testsheet'])
			newdoc.save()
			handle_uploaded_file_test(request.FILES['testsheet'])

			return HttpResponseRedirect(reverse('webapp.views.home'))
	else:
		form = AttendanceForm() # A empty, unbound form

	tests = Test.objects.all()

	return render_to_response('test.html',{'tests':tests, 'form':form},context_instance=RequestContext(request))


	



	

def handle_uploaded_file_test(f):
	#files=open(f.url, 'r')
	for line in f:
		line=line.split(',')
		tmp=TestRecord.objects.create()
		if isinstance(line[0],models.IntegerField):
			tmp.stud_ID=line[0]
		if isinstance(line[1],models.CharField):
			tmp.stud_name=line[1]
		if isinstance(line[2],models.IntegerField):
			tmp.stud_score=line[2]
		if isinstance(line[3],models.IntegerField):	
			tmp.test_no=line[3]
		if isinstance(line[4],models.IntegerField):
			tmp.test_avg=line[4]

		tmp.save()


def parent_data(request):
    # Handle file upload
	if request.method == 'POST':
		form = ParentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = ParentSheet(parentsheet = request.FILES['parentsheet'])
			newdoc.save()
			handle_uploaded_file_parent(request.FILES['parentsheet'])

			return HttpResponseRedirect(reverse('webapp.views.home'))
	else:
		form = StudentForm() # A empty, unbound form

	#tests = Test.objects.all()

	return render_to_response('parent_data.html',{'form':form},context_instance=RequestContext(request))


	



	

def handle_uploaded_file_parent(f):
	#files=open(f.url, 'r')
	
	for line in f:
		line=line.split(',')
		user = User.objects.create_user(username=line[0],password=line[1],first_name=line[2])
		user.groups.add(Group.objects.get(name='Parent'))
	

def student_data(request):
    # Handle file upload
	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = StudentSheet(studentsheet = request.FILES['studentsheet'])
			newdoc.save()
			handle_uploaded_file_student(request.FILES['studentsheet'])

			return HttpResponseRedirect(reverse('webapp.views.home'))
	else:
		form = StudentForm() # A empty, unbound form

	#tests = Test.objects.all()

	return render_to_response('student_data.html',{'form':form},context_instance=RequestContext(request))


	



	

def handle_uploaded_file_student(f):
	#files=open(f.url, 'r')
	
	for line in f:
		line=line.split(',')
		user = User.objects.create_user(username=line[0],password=line[1],first_name=line[2])
		user.groups.add(Group.objects.get(name='Student'))


def chart(request):
	stud_ID=request.user.get_username()

	testdata = \
   		DataPool(
    		series=
    		[{'options': {
    		'source': TestRecord.objects.all().filter(stud_ID=stud_ID)},
    		'terms': [
    			'test_no',
    			'stud_score',
    			'test_avg']}
    			])

    #Step 2: Create the Chart object
	cht = Chart(
		datasource = testdata,
			series_options =
			[{'options':{
					'type': 'line',
					'stacking': False},
					'terms':{
						'test_no': [
							'stud_score',
							'test_avg']
							}}],

			chart_options =
				{'title': {
					'text': 'Student Performance'},
					'xAxis': {
						'title': {
							'text': 'Test number'}}})
	return render_to_response('charts.html',{'chart' :cht})	

	

def attendance(request):
    # Handle file upload
	if request.method == 'POST':
		form = AttendanceForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Attendance(attendancesheet = request.FILES['attendancesheet'])
			newdoc.save()
			handle_uploaded_file_att(request.FILES['attendancesheet'])

            
        	return HttpResponseRedirect(reverse('webapp.views.home'))
	else:
		form = AttendanceForm() # A empty, unbound form

    # Load documents for the list page
	attendance = Attendance.objects.all()

    # Render list page with the documents and the form
	return render_to_response(
		'attendance.html',
		{'attendance':attendance, 
			'form':form},
		context_instance=RequestContext(request))

#def attendance(request):
#	return render(request,'attendance.html',{})


def handle_uploaded_file_att(f):
	#files=open(f.url, 'r')
	for line in f:
		line=line.split(',')
		tmp=AttendanceRecord.objects.create()
		tmp.stud_ID=line[0]
		tmp.stud_name=line[1]
		tmp.stud_presence=line[2]
		#tmp.attendance_no=line[3]
		tmp.save()	

def handler404(request):
	response = render_to_response('404.html', {},context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('500.html', {},context_instance=RequestContext(request))
	response.status_code = 500
	return response

'''
def handle_uploaded_file_stud(f):
	for line in f:

def student_data(request):
	if request.method=='POST':
		form=StudentForm(request.POST,request.FILES)
		if form.is_valid():
			newdoc = StudentSheet(studentsheet = request.FILES['studentsheet'])
			newdoc.save()
			handle_uploaded_file_stud(request.FILES['studentsheet'])

            
        	return HttpResponseRedirect(reverse('webapp.views.home'))
	else:
		form=StudentForm()

	#studentsheets=StudentSheet.objects.all()
	return render_to_response('student_data.html',{'form':form,},context_instance=RequestContext(request))

def handle_uploaded_file_stud(f):
	for line in f:'''
