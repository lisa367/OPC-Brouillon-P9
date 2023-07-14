from django.urls import path
from .views import CreateReviewView, UpdateReviewView, DeleteReviewView

app_name = "reviews_app"

urlpatterns = [
    path("create/", CreateReviewView.as_view(), name="create-review"),
    path("update/<int:pk>", UpdateReviewView.as_view(), name="update-review"),
    path("delete/<int:pk>", DeleteReviewView.as_view(), name="delete-review"),
]
