from django.forms import ModelForm
from myapp1.models import Registration
class UserForm(ModelForm):
	class Meta:
		model=Registration
		fields=['name','email','phno']#'__all__'
class Userlogin(ModelForm):
	class Meta:
		model=Registration
		fields=['username','password']