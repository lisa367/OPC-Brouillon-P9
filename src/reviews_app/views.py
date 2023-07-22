from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from tickets_app.forms import TicketForm


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



def create_review_and_ticket(request):
    context = {}
    if request.method == "POST":
        pass
        form_ticket = TicketForm(request.POST)
        form_review = ReviewForm(request.POST)
        form_ticket.save()
        form_review.save()
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
    
    context["form_ticket"] = form_ticket
    context["form_review"] = form_review

    return render("reviews_app/create_review_ticket.html", context=context)
