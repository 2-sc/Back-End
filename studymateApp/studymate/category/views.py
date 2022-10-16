import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from studymate.settings import SECRET_KEY
from user.models import User
from .models import Category
from .permissions import isAuthenticated
from .serializers import CategoryGetSerializer, CategoryCreateSerializer, CategoryUpdateSerializer
# Create your views here.

# 카테고리
class CategoryAllView(APIView):
    permission_classes = [isAuthenticated]
    # 카테고리 조회
    def get(self, request):
        try:
            token = request.headers['Authorization']
            user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            categorys = Category.objects.filter(email_id=user_token['id'])
            seiralizer = CategoryGetSerializer(categorys, many=True)
            print(seiralizer.data)
            return Response(seiralizer.data, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '카테고리 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    permission_classes = [isAuthenticated]
    # 과목 추가 request -> {subject}
    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.email_id = user_token['id']
            serializer.save()
            return Response({'isSuccess': True, 'msg': '카테고리 생성 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '카테고리 생성을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 과목 수정 request -> {email, subject}
    def patch(self, request, pk):
        user_token = request.headers['Authorization']
        user_decode = jwt.decode(user_token, SECRET_KEY, algorithms='HS256')
        user = User.objects.get(pk=user_decode['id'])
        category = Category.objects.get(pk=pk)
        serializer = CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            if Category.objects.filter(email_id=user.id, subject=serializer.validated_data['subject']).exists():
                return Response({'isSuccess': False, 'msg': '이미 있는 카테고리입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'isSuccess': True, 'msg': '카테고리 수정 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '카테고리 수정을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 과목 삭제
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({'isSuccess': True, 'msg': '카테고리 삭제 되었습니다.'},status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'isSuccess': False, 'msg': '카테고리 삭제를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)