from django.contrib import admin

# Register your models here.
from .models import Document
from .forms import DocumentForm
#from .views import handle_uploaded_file


from .models import Test, TestRecord,Attendance, AttendanceRecord,MonthlyWeatherByCity,  Schedules, News
from .forms import TestForm

class DocumentAdmin(admin.ModelAdmin):
	list_display=["docfile"]
	def list(request):
		if request.method=='POST':
			form=DocumentForm(request.POST, request.FILES)
			if form.is_valid():
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

class TestAdmin(admin.ModelAdmin):
	list_display=["testname","extension"]
	#form=TestForm

	'''def upload_file(request):
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				handle_uploaded_file(request.FILES['file'])
				return HttpResponseRedirect('/success/url/')
		else:
			form = UploadFileForm()
			return render(request, 'home.html', {'form': form})'''

	'''def test(request):
		if request.method=='POST':
			form=TestForm(request.POST, request.FILES)

			
			if form.is_valid() :
				handle_uploaded_file(request.FILES['testsheet'])

				return HttpResponseRedirect(reverse('webapp.admin'))

			
				
		else :
			tform=TestForm()

		tests=Test.objects.all()
	
		return render_to_response(
			'webapp.admin',
			{'tests':tests, 
			'tform':tform},
			context_instance=RequestContext(request))'''

	
class TestRecordAdmin(admin.ModelAdmin):
	list_display=["__unicode__","stud_score","test_no"]		


class AttendanceAdmin(admin.ModelAdmin):
	list_display=["attendancename","extension"]	

class AttendanceRecordAdmin(admin.ModelAdmin):
	list_display=["__unicode__","stud_presence"]

class MonthlyWeatherByCityAdmin(admin.ModelAdmin):
	list_display=[]


class NewsAdmin(admin.ModelAdmin):
	list_display=["message_ID"]

class SchedulesAdmin(admin.ModelAdmin):
	list_display=["title"]


admin.site.register(Schedules, SchedulesAdmin)	
admin.site.register(News, NewsAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
admin.site.register(TestRecord, TestRecordAdmin)
admin.site.register(MonthlyWeatherByCity, MonthlyWeatherByCityAdmin)