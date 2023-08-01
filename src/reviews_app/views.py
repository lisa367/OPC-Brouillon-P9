from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from tickets_app.forms import TicketForm
from tickets_app.models import Ticket

User = get_user_model()


class CreateReviewView(CreateView):
    template_name = "reviews_app/create_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("homepage")
    # fields = "__all__"
    # exclude = ["time_created"]
    # form_class = ReviewForm

    def get(self, request, *args, **kwargs):
        print("kwargs : ", kwargs)
        print("request : ", request)
        context = self.get_context_data(object=self.get_object(), **kwargs)
        print(context)
        super().get(request, *args, **kwargs)
        # return self.render_to_response(context)
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pk = kwargs.get("pk")
        print("request: ", self.request)
        print("kwargs: ", kwargs)
        # context["ticket"] = Ticket.objects.get(pk=pk)
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
            # user_id = User.objects.get(username=request.user).pk
            # form_ticket.cleaned_data["user"] = user_id
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # print("ticket : ", form_ticket.cleaned_data)
            #print(form_ticket["user"])
            print("ticket : ", ticket)
            last_ticket = Ticket.objects.last()

        """ if form_review.is_valid():
            form_review.cleaned_data["user"] = last_ticket.user
            form_review.cleaned_data["ticket"] = last_ticket.pk
            form_review.save()
            print("review : ", form_review.cleaned_data) """
        return redirect("homepage")

    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
        context["form_ticket"] = form_ticket
        context["form_review"] = form_review

    return render(request, "reviews_app/create_review_ticket.html", context=context)
