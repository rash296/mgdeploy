from django import forms

from .models import Test,Attendance

from .models import SignUp

class QueryForm(forms.Form):
	
	Your_email=forms.EmailField()
	Your_query = forms.CharField(widget=forms.Textarea,required=True)

class notifyForm(forms.Form):
	
	#Your_email=forms.EmailField()
	Notification_message = forms.CharField(widget=forms.Textarea,required=True)



class DocumentForm(forms.Form):
	docfile=forms.FileField(
		label="Select a file",
		help_text="max 42 MB"
		)

class TestForm(forms.Form):
	#class Meta:
	#	model=Test
	#	fields=['testsheet']

	
	testsheet=forms.FileField(
		#widget=forms.ClearableFileInputButton(attrs={'class' : 'waves-effect waves-light btn white-text'}),
		label="Select a file",
		help_text="Must be csv"
		
		)

class AttendanceForm(forms.Form):
	
	attendancesheet=forms.FileField(
		#widget=forms.ClearableFileInputButton(attrs={'class' : 'waves-effect waves-light btn white-text'}),
		label="Select a file",
		help_text="Must be csv"
		
		)



'''class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	filename = forms.FileField(label="Select a file",
		help_text="Must be csv")	'''
