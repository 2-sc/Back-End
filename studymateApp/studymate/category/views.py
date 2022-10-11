from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .models import Category
from .permissions import isAuthenticated
from .serializers import CategoryGetSerializer, CategoryCreateSerializer, CategoryUpdateSerializer
# Create your views here.

# 카테고리
class CategoryView(APIView):
    permission_classes = [isAuthenticated]
    # 카테고리 조회
    def get(self, request):
        categorys = Category.objects.filter(email=self.request.user)
        seiralizer = CategoryGetSerializer(categorys, many=True)
        return Response(seiralizer.data, status=status.HTTP_200_OK)

    # 과목 추가 request -> {subject}
    def post(self, request):
        user = User.objects.get(email=self.request.user)
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.email = user.email
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 과목 수정 request -> {email, subject}
    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 과목 삭제
    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# class StopwatchView(APIView):
#     # 과목 시간 수정 reqeust -> {id, email, subject}
#     def put(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         serializer = StopwatchSerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

