from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def chatbot_response(request):
    return Response({'response' : 'Hello, how can i help you?'})

@api_view(['POST'])
def chatbot_input(request):
    user_input = request.data.get('input')
    return Response({'response' : f'you said {user_input}'})
