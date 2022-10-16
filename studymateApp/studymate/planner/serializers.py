from rest_framework import serializers

from .models import Todo, Schedule, Comment


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo', 'complete', 'register')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule', 'register')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'register')

    def validate(self, data):
        if Comment.objects.filter(register=data['register']).exists():
            raise serializers.ValidationError({'register': '오늘의 다짐이 존재합니다.'})
        return data
