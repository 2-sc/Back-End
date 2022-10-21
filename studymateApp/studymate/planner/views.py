import jwt
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from datetime import datetime

from .models import Schedule, Comment
from .models import Todo as TodoModel
from .serializers import TodoSerializer, ScheduleSerializer, CommentSerializer, TodoDetailSerializer, \
    CommentDetailSerializer
from .permissions import isAuthenticated
from studymate.settings import SECRET_KEY
from user.models import User


# Create your views here.

# 투두리스트만 조회
class TodoAPIView(APIView):
    permission_classes = [isAuthenticated]

    def get(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        # request -> {"user_id": Int, "register": null}
        try:
            if request.data.get("register") is None:
                todo = TodoModel.objects.filter(register=datetime.now().strftime('%Y-%m-%d'),
                                                # user_id=request.data.get("user_id"))
                                                user_id=user_token['id'])
                serializer = TodoSerializer(todo, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "0000-00-00"}
            elif request.data.get("register") == "0000-00-00":
                todo = TodoModel.objects.order_by('-register').filter(user_id=user_token['id'])  # 내림차순
                serializer = TodoSerializer(todo, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "date(yyyy-mm-dd)"}
            else:
                todo = TodoModel.objects.filter(register=request.data.get("register"), user_id=user_token['id'])
                serializer = TodoSerializer(todo, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '투두 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 투두리스트 생성
class TodoCreateAPIView(APIView):
    permission_classes = [isAuthenticated]

    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user_id = user_token['id']
            serializer.save()
            return Response({'isSuccess': True, 'msg': '투두 생성 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '투두 생성을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 투두리스트 수정 및 삭제
class TodoDetailAPIView(APIView):
    permission_classes = [isAuthenticated]

    def patch(self, request, pk):
        user_token = request.headers['Authorization']
        user_decode = jwt.decode(user_token, SECRET_KEY, algorithms='HS256')
        todo = get_object_or_404(TodoModel, pk=pk)
        serializer = TodoDetailSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            todo = TodoModel.objects.get(pk=pk)
            todo.delete()
            return Response({'isSuccess': True, 'msg': '투두 삭제 되었습니다'}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'isSuccess': False, 'msg': '투두 삭제를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 스케줄 조회
class ScheduleAPIView(APIView):
    permission_classes = [isAuthenticated]

    def get(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        try:
            # request -> {"user_id": Int, "register": null}
            if request.data.get("register") is None:
                schedule = Schedule.objects.filter(register=datetime.now().strftime("%Y-%m-%d"),
                                                   user_id=request.data.get("user_id"))
                serializer = ScheduleSerializer(schedule, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "0000-00-00"}
            elif request.data.get("register") == "0000-00-00":
                schedule = Schedule.objects.filter(user_id=request.data.get("user_id")).order_by('-register')
                serializer = ScheduleSerializer(schedule, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "date(yyyy-mm-dd)"}
            else:
                schedule = Schedule.objects.filter(register=request.data.get("register"),
                                                   user_id=request.data.get("user_id"))
                serializer = ScheduleSerializer(schedule, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '스케줄 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 스케줄 생성
class ScheduleCreateAPIView(APIView):
    permission_classes = [isAuthenticated]

    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user_id = user_token['id']
            serializer.save()
            return Response({'isSuccess': True, 'msg': '스케줄 생성 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '스케줄 생성을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 스케줄 삭제
class ScheduleDetailAPIView(APIView):
    permission_classes = [isAuthenticated]

    def delete(self, request, pk):
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()
            return Response({'isSuccess': True, 'msg': '스케줄 삭제 되었습니다.'}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'isSuccess': False, 'msg': '스케줄 삭제를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 다짐 조회
class CommentAPIView(APIView):
    permission_classes = [isAuthenticated]

    def get(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        try:
            # request -> {"user_id": Int, "register": null} [0]
            if request.data.get("register") is None:
                comment = Comment.objects.filter(register=datetime.now().strftime("%Y-%m-%d"),
                                                 user_id=user_token['id'])
                serializer = CommentSerializer(comment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "0000-00-00"}
            elif request.data.get("register") == "0000-00-00":
                comment = Comment.objects.all().order_by('-register').filter(user_id=user_token['id'])
                serializer = CommentSerializer(comment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # request -> {"user_id": Int, "register": "date(yyyy-mm-dd)"}
            else:
                comment = Comment.objects.filter(register=request.data.get("register"),
                                                 user_id=user_token['id'])
                serializer = CommentSerializer(comment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '다짐 조회를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 다짐 생성
class CommentCreateAPIView(APIView):
    permission_classes = [isAuthenticated]

    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        serializer = CommentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user_id = user_token['id']
            if Comment.objects.filter(comment=serializer.validated_data['comment']).exists():
                return Response({'isSuccess': False, 'msg': '오늘의 다짐이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'isSuccess': True, 'msg': '다짐 생성 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '다짐 생성을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 다짐 수정 및 삭제
class CommentDetailAPIView(APIView):
    permission_classes = [isAuthenticated]

    def patch(self, request, pk):
        user_token = request.headers['Authorization']
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'isSuccess': True, 'msg': '다짐 수정 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '다짐 수정을 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({'isSuccess': True, 'msg': '다짐 삭제 되었습니다.'}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'isSuccess': False, 'msg': '다짐 삭제를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
