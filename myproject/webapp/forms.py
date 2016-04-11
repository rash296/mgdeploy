import re
import csv
from django import forms
from io import TextIOWrapper

from .models import Test,Attendance

from .models import SignUp


from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

        
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

class StudentForm(forms.Form):
	studentsheet=forms.FileField(
		label="Select a file",
		help_text="Must be csv"

		)

class ParentForm(forms.Form):
	parentsheet=forms.FileField(
		label="Select a file",
		help_text="Must be csv"

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


	
	

	def clean_testsheet(self):
		testsheet = self.cleaned_data.get("testsheet", False)
		filetype = testsheet.name.split('.')[1]
		#filetype = magic.from_buffer(file.read())
		print filetype
		if not "csv" in filetype:
			raise forms.ValidationError("File is not csv.")
		
		return testsheet


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
