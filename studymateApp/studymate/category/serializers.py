from .models import Category
from rest_framework import serializers
from user.models import User

class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryCreateSerializer(serializers.Serializer):
    subject = serializers.CharField(required = True)

    # def validate(self, data):
    #     if Category.objects.filter(subject=data['subject']).exists():
    #         raise serializers.ValidationError({'subject': '이미 있는 카테고리입니다.'})
    #     return data

    def create(self, validated_data):
        category = Category.objects.create(
            email_id = User.objects.get(pk=self.email_id),
            subject = validated_data['subject']
        )
        category.save()
        return category

class CategoryUpdateSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(required=True)
    class Meta:
        model = Category
        fields = ['subject', ]
