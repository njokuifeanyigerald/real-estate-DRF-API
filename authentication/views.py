from multiprocessing import AuthenticationError
from rest_framework import generics, permissions, status, response
from .models import User
from .serializer import RegisterSerializer, LoginSerializer, LogoutSerializer
from .renderers import userRenderer

from django.contrib.auth import authenticate



class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [userRenderer]
    def post(self, request, format=None):
        form_data = request.data
        serializer  = self.serializer_class(data=form_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return response.Response(serializer.data, status.HTTP_201_CREATED)
        
 

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        data = request.data
        email = data['email']
        password = data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationError('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationError('Account disabled, contact admin')
        if not user.email_verified:
            raise AuthenticationError('Email is not verified')
        if user:
            serializer = self.serializer_class(user)
            # 201 created, because it will create a refresh token and access token
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'error': 'credentials are not valid'}, status=status.HTTP_401_UNAUTHORIZED)
        

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'success': 'successfully logged out'}, status=status.HTTP_204_NO_CONTENT)
  