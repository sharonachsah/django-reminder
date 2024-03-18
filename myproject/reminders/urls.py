from django.urls import path
from .views import create_reminder, reminder_view, reminders_view

urlpatterns = [
    path('create', create_reminder),
    path('reminder', reminder_view),
    path('reminders', reminders_view),
    # Other URL patterns for your reminders app...
]