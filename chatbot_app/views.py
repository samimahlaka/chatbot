
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

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
    return Response({'response': result['response']})




