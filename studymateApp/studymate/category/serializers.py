from .models import Category
from rest_framework import serializers

class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'subject',)

class CategoryCreateSerializer(serializers.Serializer):
    subject = serializers.CharField(required = True)

    def validate(self, data):
        if Category.objects.filter(subject=data['subject']).exists():
            raise serializers.ValidationError({'subject': '이미 있는 카테고리입니다.'})
        return data

    def create(self, validated_data):
        category = Category.objects.create(
            email = self.email,
            subject = validated_data['subject']
        )
        category.save()
        return category

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['subject', ]

    def validate(self, data):
        if Category.objects.filter(subject=data['subject']).exists():
            raise serializers.ValidationError({'subject': '이미 있는 카테고리입니다.'})
        return data