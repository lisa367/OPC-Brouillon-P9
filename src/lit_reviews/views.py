# views_bis.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# from .models import UserFollows, Review, Ticket
from .forms import SignupForm, LoginForm, NewSubscriptionForm
from reviews_app.models import Review, UserFollows
from tickets_app.models import Ticket


def index(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        # if form.is_valid :
        user = authenticate(request, username=username, password=password)
        print(user)
        # if form.is_valid :
        if user:
            print("valid form")
            login(request, user)
            return redirect("homepage")
        else:
            print("invalid form")
            return redirect("index")

    else:
        # form = LoginForm()
        form = AuthenticationForm()
        context["form"] = form
        return render(request, "lit_reviews/index.html", context=context)


def signup(request):
    context = {}
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print("user")
            login(request, user)
            return redirect("homepage")
        else:
            print("invalid form")
            return redirect("index")
    else:
        # form = SignupForm()
        form = UserCreationForm()
        context["form"] = form
        return render(request, "lit_reviews/signup.html", context=context)


@login_required
def homepage(request):
    context = {}
    user = User.objects.get(username=request.user.username)
    form = NewSubscriptionForm()
    reviews = Review.objects.filter(user_id=user.pk)
    tickets = Ticket.objects.filter(user_id=user.pk)
    user_follows = UserFollows.objects.filter(user_id=user.pk)
    followers = UserFollows.objects.filter(followed_user_id=user.pk)
    followers_posts = Review.objects.filter()

    context["form"] = form
    context["reviews"] = reviews
    context["tickets"] = tickets
    context["user_follows"] = user_follows
    # context["followers"] = followers
    return render(request, "lit_reviews/homepage.html", context=context)


@login_required
def subscriptions(request):
    context = {}
    if request.method == "POST":
        # form = NewSubscriptionForm()
        form = NewSubscriptionForm(request.POST)
        if form.is_valid():
            form = NewSubscriptionForm(request.POST)
    else:
        form = NewSubscriptionForm()
        user = User.objects.get(username=request.user.username)
        followers_ids = UserFollows.objects.filter(followed_user=user.pk)
        followers = [User.objects.get(pk=user_id).username for user_id in followers_ids]
        followed_users = UserFollows.objects.filter(user=user.pk)

        context["form"] = form
        context["followed_users"] = followed_users
        context["followers"] = followers
        return render(request, "lit_reviews/user_follows.html", context=context)


def unfollow(request, subs_username):
    user_name = request.user.username
    user = User.objects.get(username=user_name)
    followed_user = User.objects.get(username=subs_username)
    user_subcription = UserFollows.objects.filter(
        user=user.pk, followed_user=followed_user.pk
    )
    user_subcription.delete()
    return redirect("homepage")


@login_required
def posts(request):
    reviews = Review.objects.all().order_by("-time_created")[0:5]
    tickets = Ticket.objects.all().order_by("-time_created")[0:5]
    context = {"reviews": reviews, "tickets": tickets}
    return render(request, "lit_reviews/posts.html", context=context)


""" 
@login_required
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect("homepage")
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        pass
"""


def logout_view(request):
    logout(request)
    return redirect("index")
