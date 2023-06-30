from django.urls import path
from .views import CreateTicketView, UpdateTicketView, DeleteTicketView

urlpatterns = [
	path('create/', CreateTicketView.as_view(), name="create-ticket"),
	path('update/<ticket_id>', UpdateTicketView.as_view(), name="update-ticket"),
	path('delete/<ticket_id>', DeleteTicketView.as_view(), name="delete-ticket"),
]