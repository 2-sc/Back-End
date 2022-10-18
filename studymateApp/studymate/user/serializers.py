from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            password = validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# 로그인
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        models = User,
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nickname', 'image', 'info', 'page', 'd_day_start', 'd_day_end', 'd_day']