# from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm


class CreateReviewView(CreateView):
    template_name = "reviews_app/create_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("homepage")
    # fields = "__all__"
    # exclude = ["time_created"]
    # form_class = ReviewForm


class UpdateReviewView(UpdateView):
    template_name = "reviews_app/update_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("homepage")
    # fields = "__all__"
    # exclude = ["time_created"]


class DeleteReviewView(DeleteView):
    template_name = "reviews_app/delete_review.html"
    model = Review
    success_url = reverse_lazy("homepage")
    # fields = "__all__
