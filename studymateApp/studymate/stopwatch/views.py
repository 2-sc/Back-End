import jwt
from datetime import datetime
from rest_framework.views import APIView, status
from rest_framework.response import Response
from category.models import Category

from .models import StopWatch

from .serializers import StopWatchEndSerializer, StopWatchSerializer, StopWatchStartSerializer
from .permissions import isAuthenticated
from user.models import User
from studymate.settings import SECRET_KEY

# Create your views here.

class TotalView(APIView):
    permission_classes = [isAuthenticated]

    # 일단 오늘 새벽이나 내일 해서 당일것만 뜨는지 확인해보기
    def get(self, request):
        try:
            token = request.headers['Authorization']
            user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            time_log = StopWatch.objects.filter(email_id=user_token['id'], register_dttm=datetime.now().strftime("%Y-%m-%d"))
            total = '00:00:00'
            serializer = StopWatchSerializer(time_log, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '로그 조희를 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

class StopWatchView(APIView):
    permission_classes = [isAuthenticated]

    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        user = User.objects.get(pk=user_token['id'])
        serializer = StopWatchStartSerializer(data=request.data)
        if serializer.is_valid():
            if Category.objects.filter(email_id=user.id, subject=request.data['subject']).exists():
                serializer.email_id = user.id
                serializer.save()
                return Response({'isSuccess': True, 'msg': '스탑워치 시작'}, status=status.HTTP_201_CREATED)
        return Response({'isSuccess': False, 'msg': '스탑워치 시작되지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            time_log = StopWatch.objects.get(pk=pk)
            if time_log['endTime'] != '00:00:00':
                return Response({'isSuccess': False, 'msg': '스탑워치를 먼저 시작해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = StopWatchEndSerializer(time_log, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'isSuccess': True, 'msg': '스탑워치 종료'}, status=status.HTTP_200_OK)
        except:
            return Response({'isSuccess': False, 'msg': '스탑워치 종료되지 않습니다.'})