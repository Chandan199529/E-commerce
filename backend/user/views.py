from django.shortcuts import render

from .serializer import UserSerializer,RegisterSerializer,JwtTokenSerializer
from .models import User,Profile

from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=JwtTokenSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]    
    
@api_view(['GET','POST']) 
@permission_classes([IsAuthenticated])
def Dashboard(request):
    if request.method == 'GET':
        context = f'Hi {request.user}, here is your data'
        return Response({'response':context},status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        text = request.POST.get("text")
        resposne = f'Hi {request.user}, Your Text is {text}' 
        return Response({'response':resposne},status=status.HTTP_200_OK)   
   
    return Response({},status=status.HTTP_400_BAD_REQUEST)
    