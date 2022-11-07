from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model

from . import serializers
# Create your views here.

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset= UserModel.objects.all()
    default_serializer_class = serializers.UserOutputSerializer
    
    
    serializers_classes = {
        "create":serializers.UserInputSerializer
    }
    
    def create(self, request, *args, **kwags):
        
        """_summary_
            User Sign up option
        Args:
            request (_type_): _description_
        """
        
        self.check_permissions(request)
        serializer = serializers.UserInputSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        user = userModel.objects.create_user(
            email = serializer.validated_data["email"],
            first_name = serializer.validated_data["first_name"],
            last_name = serializer.validated_data["last_name"],
            password = serializer.validated_data["password"]
        )
        
        response = serializers.UserOutputSerializer(user).data
        return Response(response, status=status.HTTP_201_CREATED)
         
        

    
    def get_permission(self):
        if self.action =='create': #create, list,retrieve
            permission_classes =  [permissions.AllowAny]
        elif self.action=='retrieve':
            permission_classes=[permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update','destroy']:
            permission_classes = [IsCreatorOrAdminReadOnly, permissions.Authenticated ]
        elif self.action =='list':
            permission_classes[permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]
        
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)