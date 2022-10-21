from rest_framework import serializers

from user.models import User
from .models import Todo as TodoModel
from .models import Schedule as ScheduleModel
from .models import Comment as CommentModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('user_id', 'todo', 'complete', 'register')

    def create(self, validated_data):
        todo = TodoModel.objects.create(
            user_id=User.objects.get(pk=self.user_id),
            todo=validated_data['todo'],
            complete=validated_data['complete'],
            register=validated_data['register']
        )
        todo.save()
        return todo


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('complete',)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = ('schedule', 'register')

    def create(self, validated_data):
        schedule = ScheduleModel.objects.create(
            user_id=User.objects.get(pk=self.user_id),
            schedule=validated_data['schedule'],
            register=validated_data['register']
        )
        schedule.save()
        return schedule


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('user_id', 'comment', 'register')

    def create(self, validated_data):
        comment = CommentModel.objects.create(
            user_id=User.objects.get(pk=self.user_id),
            comment=validated_data['comment'],
            register=validated_data['register']
        )
        comment.save()
        return comment


class CommentDetailSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(required=True)

    class Meta:
        model = CommentModel
        fields = ("comment",)


class LogCommentSerializer(serializers.ModelSerializer):
    temp_todo = TodoSerializer(many=True)

    class Meta:
        model = CommentModel
        fields = ('user_id', 'comment', 'register', 'temp_todo',)


class LogTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('todo', 'complete',)
