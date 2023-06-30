from django.urls import path
from .views import CreateReviewView, UpdateReviewView, DeleteReviewView

urlpatterns = [
	path('create/', CreateReviewView.as_view(), name="create-critique"),
	path('update/<review_id>', UpdateReviewView.as_view(), name="update-critique"),
	path('delete/<review_id>', DeleteReviewView.as_view(), name="delete-critique"),
]