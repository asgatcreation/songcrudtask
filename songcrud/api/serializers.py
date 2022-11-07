from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

#from symbol import return_stmt

UserModel = get_user_model()

class UserInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only = True)
    
    slug = serializers.SlugField(required = True)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    email=serializers.CharField(required=True)
    
    class Meta:
        model = UserModel
        field = ('email', 'first_name', 'last_name','password', 'password2', 'slug')
        
    def validate(self, attrs):
        if attrs['password']!= attrs['password2']:
            raise serializers.ValisationErrorUser
        return super().validate(attrs)
    
class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name','last_name', 'slug')