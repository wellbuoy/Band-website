from django.contrib import admin

# Import the Event, Question and Choice model from the models module in the current directory
from .models import Event

# Register the Event model with the admin site
admin.site.register(Event)
