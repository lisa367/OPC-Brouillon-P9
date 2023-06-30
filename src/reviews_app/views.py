from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm

class CreateReviewView(CreateView):
	template_name = "critiques_app/create_review.html"
	model = Review
	form_class = ReviewForm
    # fields = "__all__"
		# exclude = ["time_created"]
		# form_class = ReviewForm

class UpdateReviewView(UpdateView):
	template_name = "critiques_app/update_review.html"
	model = Review
	form_class = ReviewForm
    # fields = "__all__"
		# exclude = ["time_created"]

class DeleteReviewView(DeleteView):
	template_name = "critiques_app/delete_review.html"
	model = Review
	success_url = reverse_lazy("homepage")
    # fields = "__all__
