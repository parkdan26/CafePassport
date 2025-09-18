# user/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username = email, password = password)
        if user: 
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            response = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            response.set_cookie(
                    key="access_token",
                    value=access_token,
                    httponly=True,
                    secure=True,        
                    samesite="None",  
                    max_age=60*15       
                )
            response.set_cookie(
                    key="refresh_token",
                    value=refresh_token,
                    httponly=True,
                    secure=True,
                    samesite="None",
                    max_age=60*60*24*15  
                )
                
            return response    
            
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response

class RefreshView(APIView): 
    permission_classes = [AllowAny]

    def post(self, request): 
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "No refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            token = RefreshToken(refresh_token)
            new_refresh = RefreshToken.for_user(token.user) 
            new_access = new_refresh.access_token 
            response = Response({"detail": "new token given"}, status=status.HTTP_200_OK)
            response.set_cookie(
                    key="access_token",
                    value= new_access,
                    httponly=True,
                    secure=True,        
                    samesite="None",  
                    max_age=60*15       
                )
            response.set_cookie(
                    key="refresh_token",
                    value= new_refresh,
                    httponly=True,
                    secure=True,
                    samesite="None",
                    max_age=60*60*24*15  
                )
            token.blacklist()
            return response
        except: 
            return Response({"detail": "Invalid refresh token"}, status=401)
