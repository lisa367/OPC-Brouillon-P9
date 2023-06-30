from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
	model = User
	# fields = ["username", "password"]

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2",]