
from django.urls import path
from chatbot_app import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('chatbot_input/', views.chatbot_input),
    path('chatbot_list/' , views.chatbot_list),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
    path('redis_test/',views.redis_test),
]
