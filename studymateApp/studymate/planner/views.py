from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.

# 투두리스트만 조회
class TodoAPIView(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializers = TodoSerializer(todo, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# 투두리스트 생성
class TodoCreateAPIView(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'isSuccess': True, 'msg': '투두 생성 되었습니다.'}, status=status.HTTP_200_OK)
        return Response({'isSuccess': False, 'msg': '투두 생성을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 투두리스트 수정 및 삭제
class TodoDetailAPIView(APIView):
    def patch(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'isSuccess': True, 'msg': '투두 수정 되었습니다.'}, status=status.HTTP_200_OK)
        return Response({'isSuccess': False, 'msg': '투두 수정을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        if todo is not None:
            return Response({'isSuccess': True, 'msg': '투두 삭제 되었습니다'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'isSuccess': False, 'msg': '투두 삭제를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
