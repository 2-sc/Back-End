from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt import TokenObtainPairSerializer

from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from .models import User

# Create your views here.

# 회원가입
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        token = TokenObtainPairSerializer.get_token(user)
        
        
        

# 로그인
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        seiralizer = self.get_serializer(data=request.data)
        seiralizer.is_valid(raise_exception=True)
        token = seiralizer.validated_data

        return Response({'token': token.key}, status=status.HTTP_200_OK)

# 로그아웃 손 봐야할듯
        
# 프로필
class UserProfileView(APIView):
    permission_classes = [isAuthenticated]

    # 프로필 조회
    def get(self, request, pk):
        user_profile = User.objects.get(pk=pk)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 프로필 수정  request -> {id, email, nickname, image, info, d_day}
    def put(self, request, pk):
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