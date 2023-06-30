from django.db import models as m
from django.urls import reverse
from django.contrib.auth.models import User
from lit_reviews.settings import AUTH_USER_MODEL
from tickets_app.models import Ticket

class Review(m.Model):
	# ticket = m.CharField(max_length=128)
	ticket = m.ForeignKey(to=Ticket, on_delete=m.CASCADE)
	rating = m.PositiveSmallIntegerField(max_length=1024, validators=[m.MinValueValidator(0), m.MaxValueValidator(5)])
	user = m.ForeignKey(to=AUTH_USER_MODEL, on_delete=m.CASCADE)
	headline = m.CharField(max_length=128)
	body = m.TextField(max_length=8192)
	time_created = m.DateTimeField(auto_now_add=True)
	
	def get_absolute_url(self):
		return reverse("homepage")