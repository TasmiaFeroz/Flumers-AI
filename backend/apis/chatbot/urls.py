# chatbot/urls.py
# Import necessary modules and the chatbot response view
from django.urls import path
from .views import chatbot_response

# Define URL patterns for the chatbot application
urlpatterns = [
    # Route for the chatbot response API
    path('chat/', chatbot_response, name='chatbot_response'),
]
