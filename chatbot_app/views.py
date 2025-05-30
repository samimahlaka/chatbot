
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from .models import Conversation
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import redis

r = redis.Redis(host='localhost' , port=6379 , db=0 )

@api_view(['GET'])
def chatbot_response(request):
    return Response({'response' : 'Hello, how can i help you?'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
    Conversation.objects.create(user= request.user ,  user_input =  user_input , response = reply )
    return Response({'response': reply})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chatbot_list(request):
    conversations = Conversation.objects.filter(user=request.user)
    data = []
    for conversation in conversations:
        data.append({'user-input' : conversation.user_input,
                    'chatbot_response' : conversation.response})
        
    return Response(data)

@api_view(['GET'])
def redis_test(request):
    r.set("test", "hello i'm ready")
    
    value = r.get('test')
    result = value.decode('utf-8')
    
    return Response({"redis-value" : result})    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        access_token = data.get('access')
        username = self.user.username
        r.set(f'token : {username}' , access_token, ex=3600)
        return data
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    