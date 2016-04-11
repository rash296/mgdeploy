from __future__ import unicode_literals

from django.db import models
import os

# Create your models here.

class Document(models.Model):
	docfile=models.FileField(upload_to="documents/%d")
	#timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	def docname(self):
   		return os.path.basename(self.docfile.name)

class TestRecord(models.Model):
	stud_ID=models.IntegerField(null=True)
	stud_name=models.CharField(max_length=30,null=True)
	stud_score=models.IntegerField(null=True)
	test_no=models.IntegerField(null=True)
	test_avg=models.IntegerField(null=True)

	class Meta:
		unique_together=(('stud_ID','test_no'),)

	def __unicode__(self):
		return self.stud_name

class StudentSheet(models.Model):
	studentsheet=models.FileField(upload_to="student/%Y/%m/%d")

class ParentSheet(models.Model):
	parentsheet=models.FileField(upload_to="parent/%Y/%m/%d")	

class News(models.Model):
	message_ID=models.IntegerField(null=True)
	message=models.CharField(max_length=200)	
   
class Test(models.Model):
	testsheet=models.FileField(upload_to="test/%Y/%m/%d")	
	
	def testname(self):
   		return os.path.basename(self.testsheet.name)

   	def extension(self):
   		name,extension= os.path.splitext(self.testsheet.name)
   		return extension	
'''
	def extension(self):
   		name, extension = os.path.splitext(self.testsheet.name)
    	return extension'''

class Attendance(models.Model):
	attendancesheet=models.FileField(upload_to="attendance/%Y/%m/%d")	
	
	def attendancename(self):
   		return os.path.basename(self.attendancesheet.name)

   	def extension(self):
   		name,extension= os.path.splitext(self.attendancesheet.name)
   		return extension	


class AttendanceRecord(models.Model):
	stud_ID=models.IntegerField(null=True)
	stud_name=models.CharField(max_length=30,null=True)
	stud_presence=models.IntegerField(null=True)
	attendance_no=models.IntegerField(null=True)

	class Meta:
		unique_together=(('stud_ID','attendance_no'),)

	def __unicode__(self):
		return self.stud_name

class SignUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=120,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.email		


class MonthlyWeatherByCity(models.Model):
	month = models.IntegerField()
	boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
	houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

	#def __unicode__(self):
	#	return self.month

class Schedules(models.Model):
	date=models.DateField(auto_now=False, auto_now_add=False)
	title=models.CharField(max_length=50,null=True)
	batch=models.IntegerField(null=True)