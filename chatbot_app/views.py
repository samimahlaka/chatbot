
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import Conversation
@api_view(['GET'])
def chatbot_response(request):
    return Response({'response' : 'Hello, how can i help you?'})


@api_view(['POST'])
def chatbot_input(request):
    user_input = request.data.get('input')

    response = requests.post (
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_input,
            "stream": False
        }
    )
    result = response.json()
    reply = result['response']
    Conversation.objects.create(user_input =  user_input , response = reply )
    return Response({'response': reply})

@api_view(['GET'])
def chatbot_list(request):
    conversations = Conversation.objects.all()
    data = []
    for conversation in conversations:
        data.append({'user-input' : conversation.user_input,
                    'chatbot_response' : conversation.response})
        
    return Response(data)
    