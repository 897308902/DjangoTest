# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	class Meta:
		db_table='teacher'

		
class Student(models.Model):
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	age=models.IntegerField()
	intine=models.DateTimeField()
	sex=models.IntegerField()
	teacher=models.ForeignKey(Teacher,related_name='student_teacher')
	class Meta:
		db_table = 'student'


