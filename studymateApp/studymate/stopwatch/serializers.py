from rest_framework import serializers
from .models import StopWatch
from datetime import datetime, timedelta

class StopWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopWatch
        fields = '__all__'

class StopWatchStartSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    register_dttm = serializers.DateTimeField(default='0000-00-00')

    def create(self, validated_data):
        stopwatch = StopWatch.objects.create(
            email = self.email,
            subject = validated_data['subject'],
            startTime = datetime.now().strftime('%H:%M:%S'),
            endTime = '00:00:00',
            totalTime = '00:00:00',
            register_dttm = validated_data['register_dttm']
        )
        stopwatch.save()
        return stopwatch

class StopWatchEndSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    register_dttm = serializers.DateField(default=datetime.now().strftime('%Y-%m-%d'))

    # self -> 전달된 데이터, instance -> 기존에 저장된 데이터
    # update 라서 instance 데이터만 변경해주고 리턴해주면 됨
    def update(self, instance, validated_data):
        endTime = datetime.now().strftime('%H:%M:%S')
        startTime = datetime.strptime(str(instance.startTime), '%H:%M:%S')
        time = datetime.strptime(endTime, '%H:%M:%S') - timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)
        instance.endTime = str(endTime)
        instance.totalTime = str(time.time())
        instance.register_dttm = validated_data['register_dttm']
        instance.save()
        return instance



