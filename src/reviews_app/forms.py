from django.forms import ModelForm, RadioSelect
from .models import Review

class ReviewForm(ModelForm):
	pass
	class Meta:
		model = Review
		exclude = ["ticket", "time_created", "user",]
		widgets = {"rating": RadioSelect}
		# labels = {"": ()}