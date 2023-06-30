# views_bis.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserFollows, Review, Ticket
from .forms import SignupForm, LoginForm, NewSubscriptionForm
from reviews_app.models import Review

def index(request):
	context = {}
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		# if form.is_valid :
		if user:
			login(request, user)
			return redirect("homepage")
		
	else:
		form = LoginForm()
		context["form"] = form
		return render(request, "lit_reviews/index.html", context=context)

def signup(request):
	context = {}
	if request.method == "POST":
		pass
	else:
		form = SignupForm()
		context["form"] = form
		return render(request, "lit_reviews/signup.html", context=context) 

@login_required
def homepage(request):
	context = {}
	user = User.objects.get(username=request.user.username)
	form = NewSubscriptionForm()
	reviews = Review.objects.get(user=user)
	tickets = Ticket.objects.get(user=user)
	user_follows = UserFollows.objects.get(user=user)
	followers = UserFollows.objects.get(followed_user=user)

	context["form"] = form
	context["reviews"] = reviews
	context["tickets"] = tickets
	context["user_follows"] = user_follows
	return render(request, "lit_reviews/homepage.html", context=context)

@login_required
def subscriptions(request):
	form = NewSubscriptionForm()
	form = NewSubscriptionForm(request.POST)
	if form.is_valid():
		form = NewSubscriptionForm(request.POST)

@login_required
def posts(request):
	template_name = "lit_reviews/user_page.html"
	model = Review
	context_object_name = "post"

@login_required
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        pass
    else:
        # Return an 'invalid login' error message.
        pass

def logout_view(request):
	logout(request)
	return redirect("index")