from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .jwt import create_access_token, create_refrest_token
from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from .models import User
from .permissions import isAuthenticated


# Create your views here.

# 회원가입
class RegisterView(APIView):
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            email=request.data.get('email'), 
            password=request.data.get('password')
            )
        if user is not None:
            serilaizer = LoginSerializer(user)
            access_token = create_access_token(user)
            refresh_token = create_refrest_token(user)
            
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
class LogoutView(APIView):
    permission_classes = [isAuthenticated]

    def get(self, request):
        res = Response(
            {
                'isSuccess': True,
                'msg': '로그아웃 되었습니다.'
            },
            status=status.HTTP_200_OK
        )

        return res

        
# 프로필
class UserProfileView(APIView):
    permission_classes = [isAuthenticated]

    # 프로필 조회
    def get(self, request, pk):
        try:
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
        except ObjectDoesNotExist:
            return Response({'isSuccess': False, 'msg': '유저 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 프로필 수정
    def patch(self, request, pk):
        user_profile = User.objects.get(pk=pk)
        self.check_object_permissions(self.request, user_profile)
        if not('@' in request.data['email']):
            return Response({'isSuccess': False, 'msg': '이메일 형식이 아닙니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['email'] != user_profile.email and User.objects.filter(email=request.data["email"]).exists():
            return Response({'isSuccess': False, 'msg': '이미 존재하는 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['nickname'] != user_profile.nickname and User.objects.filter(nickname=request.data["nickname"]).exists():
            return Response({'isSuccess': False, 'msg': '이미 존재하는 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'isSuccess': True, 'msg': '프로필이 수정되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '프로필 수정을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
    # 프로필 삭제
    def delete(self, request, pk):
        try:
            user_profile = User.objects.get(pk=pk)
            self.check_object_permissions(self.request, user_profile)
            user_profile.delete()
            return Response({'isSuccess': True, 'msg': '회원 탈퇴 되었습니다.'}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'isSuccess': True, 'msg': '회원 탈퇴를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)