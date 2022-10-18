import jwt
from datetime import datetime, timedelta
from rest_framework.views import APIView, status
from rest_framework.response import Response

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
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        user = User.objects.get(pk=user_token['id'])
        time_log = StopWatch.objects.filter(email=user.email)
        total = '00:00:00'
        serializer = StopWatchSerializer(time_log, many=True)
        for i in range(len(serializer.data)):
            if(serializer.data[i]['register_dttm'] == datetime().now().strftime('%Y-%m-%d')):
                time = datetime.strptime(serializer.data[i]['totalTime'],'%H:%M:%S')
                if i == 0:
                    total = time
                else:
                    total += timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
        return Response(total.time())

class StopWatchView(APIView):
    permission_classes = [isAuthenticated]

    def post(self, request):
        token = request.headers['Authorization']
        user_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        user = User.objects.get(pk=user_token['id'])
        serializer = StopWatchStartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.email = user.email
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        time_log = StopWatch.objects.get(pk=pk)
        serializer = StopWatchEndSerializer(time_log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)