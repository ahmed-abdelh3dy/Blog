from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        image = request.data.get('image')
        phone = request.data.get('phone')
        age = request.data.get('age')

        if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(email=email).exists():
            return Response({'message': 'Username or email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create(
            username=username,
            name=name,
            email=email,
            password=make_password(password),
            image=image,
            phone=phone,
            age =age
        )

        refresh = RefreshToken.for_user(user)


        # token = Token.objects.create(user=user)

        serialized_user = UserSerializer(user)

        return Response({
            'message': 'User created',
            'user': serialized_user.data,
            'token': str(refresh),
            'access':str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)




class LoginView(APIView):
    def  post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(username=username, password=password) 
            if user:
                # token, _ = Token.objects.get_or_create(user=user)
                refresh = RefreshToken.for_user(user)

                serialized_user = UserSerializer(user)
                return Response({
                    'message': 'Login successful',
                    'user': serialized_user.data,
                    'token': str(refresh),
                    'access':str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            


    def get  (self, request):    

         users = CustomUser.objects.all()
         data = UserSerializer(users , many = True)
         return Response({'users list': data.data}, status=status.HTTP_200_OK)


        
    