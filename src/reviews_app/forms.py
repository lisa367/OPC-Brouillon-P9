from django.forms.models import ModelForm
from .models import Review

class ReviewForm(ModelForm):
	pass
	class Meta:
		model = Review
		exclude = ["ticket", "time_created", "user",]
		widget = {"rating":""}
		label = {}