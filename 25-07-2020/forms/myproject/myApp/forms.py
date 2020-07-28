from django.forms import ModelForm
from myApp.models import Student

class StudentForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'#['stuid','stuName','branch','age']