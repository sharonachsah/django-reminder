# Import necessary modules
from django.db import models

# Define the Reminder model
class Reminder(models.Model):
    datetime = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"Reminder at {self.datetime}: {self.message}"
