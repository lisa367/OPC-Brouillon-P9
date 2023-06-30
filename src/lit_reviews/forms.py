from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
	pass
	# model = User
	# fields = ["username", "password"]

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2",]

class NewSubscriptionForm(forms.Form):
	user_to_follow = forms.CharField(max_length=256)