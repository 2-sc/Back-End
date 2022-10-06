from rest_framework import permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class isAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.method == permissions.SAFE_METHODS):
            return True
        else:
            user = TokenObtainPairSerializer(request.user)
            return user.is_authenticated
    # 객체별 권환 설정
    def has_object_permission(self, request, view, obj):
        if (request.method == permissions.SAFE_METHODS):
            return True
        else:
            # GET을 제외한 요청은 작성자만 접근 가능
            print(request.user)
            print(obj.author)
            return request.user == obj.author