from rest_framework_simplejwt.tokens import Token
from .models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        
class JwtToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token =  super().get_token(user)   
        
        token['name'] = user.profile.name  
        token['username'] = user.username     
        token['email'] = user.email     
        token['bio'] = user.profile.bio     
        token['image'] = user.profile.image     
        token['varified'] = user.profile.varified   
        
        return token
      
           