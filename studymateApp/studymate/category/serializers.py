from .models import Category
from rest_framework import serializers

class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('subject',)

    # def update(self, instance, validated_data):
    #     print(self.pk)
    #     category = Category.objects.get()
    #     update_category = category.update(
    #         email = self.email,
    #         subject = validated_data['subject'],
    #         time = self.time,
    #         register_dttm = self.register_dttm
    #     )
    #     update_category.save()
    #     return update_category

class CategoryCreateSerializer(serializers.Serializer):
    subject = serializers.CharField(required = True)

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
        fields = ['id', 'email', 'subject', 'time', 'register_dttm']

    

# class StopwatchSerializer(serializers.ModelSerializer):
#     subject = serializers.CharField(required = True)
#     time = serializers.IntegerField(required = True)
    
#     class Meta:
#         model = Category
#         fields = ('id', 'email', 'subject', 'time')

#     def update(self, instance, validated_data):
#         category = Category.objects.get(pk=instance.pk)
#         update_category = Category.objects.update(
#             email = validated_data['email'],
#             subject = validated_data['subject'],
#             time = category.time + validated_data['time']
#         )
#         update_category.save()
#         return update_category
