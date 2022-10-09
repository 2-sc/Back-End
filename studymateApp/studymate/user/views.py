from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from .models import User


# Create your views here.

# 회원가입
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            res = Response(
                {
                    'isSuccess': True,
                    'msg': '회원가입이 성공되었습니다.'
                },
                status = status.HTTP_201_CREATED
            )
            return res
        return Response({'isSuccess': False, 'msg': '회원가입이 실패되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

# 로그인
class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            email=request.data.get('email'), 
            password=request.data.get('password')
            )
        
        if user is not None:
            serilaizer = LoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            
            res = Response(
                {
                    'isSuccess': True,
                    'tokenExistence': True,
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'msg': '로그인 되었습니다.'
                },
                status = status.HTTP_200_OK
            )
            return res
        return Response({'isSuccess': False, 'msg': '로그인이 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

# 로그아웃 손 봐야할듯
        
# 프로필
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    # 프로필 조회
    def get(self, request, pk):
        user_profile = User.objects.get(pk=pk)
        serializer = ProfileSerializer(user_profile)
        res = Response(
            {
                'id': serializer.data['id'],
                'nickname': serializer.data['nickname'],
                'email': serializer.data['email'],
                'image': serializer.data['image'],
                'info': serializer.data['info'],
            },
            status=status.HTTP_200_OK
        )
        if res:
            return res
        return Response({'isSuccess': False, 'msg': '유저 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 프로필 수정
    def patch(self, request, pk):
        user_profile = User.objects.get(pk=pk)
        serializer = ProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원 삭제
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)