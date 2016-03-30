from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QueryForm
from django.core.mail import send_mail
from django.conf import settings

from chartit import DataPool, Chart
import simplejson


from .models import Document,TestRecord, Test,Attendance, AttendanceRecord,MonthlyWeatherByCity, NewsFeed
from .forms import DocumentForm, TestForm, AttendanceForm, QueryForm, notifyForm


# Create your views here.

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
	testset=TestRecord.objects.all().filter(stud_ID=1).order_by('test_no')
	'''count
	attset=AttendanceRecord.objects.all().filter(stud_ID=20)

	for i in attset:
		if i.stud_presence=1:
			count=count+1'''
	testdata = \
		DataPool(
			series=
			[{'options': {
				'source': TestRecord.objects.all().filter(stud_ID=1)},
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
		
	context={
		"testset": testset,
		'chart': cht
		#"count": count,
	}
	return render_to_response('profile.html',context)


def home(request):
	'''f=open('/home/rashmi/score.csv','r')
	for line in f:
		line=line.split(',')
		tmp=TestRecord.objects.create()
		tmp.stud_ID=line[0]
		tmp.stud_name=line[1]
		tmp.stud_score=line[2]
		tmp.save()


	f.close()'''
	news=NewsFeed.objects.all()
	return render(request,'home.html',{'news':news})


def about(request):
	return render(request,'about.html',{})

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
		form = TestForm() # A empty, unbound form

    # Load documents for the list page
	tests = Test.objects.all()

    # Render list page with the documents and the form
	return render_to_response(
		'test.html',
		{'tests':tests, 
			'form':form},
		context_instance=RequestContext(request))
	
'''def test(request):
	if request.method == 'POST':
		form = TestForm(request.POST, request.FILES)
		if form.is_valid():
				#handle_uploaded_file(request.FILES['filename'])
			newdoc=Document(testsheet=request.FILES['testsheet'])
			newdoc.save()
			return HttpResponseRedirect(reverse('webapp.views.test'))
	else:
		form = TestForm()
		return render_to_response('test.html',{'form':form},context_instance=RequestContext(request))'''

def handle_uploaded_file_test(f):
	#files=open(f.url, 'r')
	for line in f:
		line=line.split(',')
		tmp=TestRecord.objects.create()
		tmp.stud_ID=line[0]
		tmp.stud_name=line[1]
		tmp.stud_score=line[2]
		tmp.test_no=line[3]
		tmp.test_avg=line[4]
		tmp.save()
	

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

'''
def handle_uploaded_file(fl):
	f=open('/home/rashmi/score.csv','r')
	for line in f:
		line=line.split(',')
		tmp=TestRecord.objects.create()
		tmp.stud_ID=line[0]
		tmp.stud_name=line[1]
		tmp.stud_score=line[2]
		tmp.save()


	f.close()	'''
'''
def handle_uploaded_file(f):
	files=open('', 'wb+')
	
    for line in files:
    	line =  line.split(',')
    	tmp = TestRecord.objects.create()
    	tmp.stud_ID = line[0]
    	tmp.stud_name = line[1]
    	tmp.stud_score= line[2]
    	tmp.save()

    files.close()'''

'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('webapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


'''




'''def chart(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
	testdata = \
        DataPool(
          	series=
            [{'options': {
               'source': TestRecord.objects.all().filter(stud_ID=1)},
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

    #Step 3: Send the chart object to the template.
    return render_to_response('charts.html',{})'''