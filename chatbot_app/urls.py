
from django.urls import path
from chatbot_app import views

urlpatterns = [
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('chatbot_input/', views.chatbot_input)
]
