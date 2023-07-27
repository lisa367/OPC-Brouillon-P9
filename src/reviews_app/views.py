from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from tickets_app.forms import TicketForm
from tickets_app.models import Ticket


class CreateReviewView(CreateView):
    template_name = "reviews_app/create_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("homepage")
    # fields = "__all__"
    # exclude = ["time_created"]
    # form_class = ReviewForm

    def get_context_data(self, ticket_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket"] = Ticket.objects.get(ticket=ticket_id)
        return context


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
        form_ticket = TicketForm(request.POST)
        form_review = ReviewForm(request.POST)
        print(form_ticket.is_valid(), form_review.is_valid())
        
        if form_ticket.is_valid():
            form_ticket.save(commit=False)
            print("ticket : ", form_ticket.cleaned_data)
        if form_review.is_valid():
            form_review["ticket"] = ''
            form_ticket.save(commit=False)
            print("review : ", form_review.cleaned_data)
        return redirect("homepage")
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
        context["form_ticket"] = form_ticket
        context["form_review"] = form_review

    return render(request, "reviews_app/create_review_ticket.html", context=context)
