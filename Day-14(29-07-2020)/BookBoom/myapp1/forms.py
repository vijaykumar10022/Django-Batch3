from django.forms import ModelForm
from myapp1.models import Registration,Mybooks
class UserForm(ModelForm):
	class Meta:
		model=Registration
		fields=['name','email','phno']#'__all__'
class Userlogin(ModelForm):
	class Meta:
		model=Registration
		fields=['username','password']
class Books(ModelForm):
	class Meta:
		model=Mybooks
		fields='__all__'
