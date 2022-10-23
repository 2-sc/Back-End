import jwt
from rest_framework.response import Response
from rest_framework import permissions

from studymate.settings import SECRET_KEY


class isAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS):
            return True
        else:
            jwt_token = request.headers['Authorization']
            if jwt_token == 'Token':  # 토큰이 없을 경우 (로그인 X)
                print('로그인 안함')
                return False  # Response({'msg': '유효하지 않은 토큰입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
            return True

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS):
            return True
        else:
            jwt_token = request.headers.get('Authorization')
            # try:
            decoded_jwt_token = jwt.decode(
                jwt_token, SECRET_KEY, algorithms='HS256'
            )
            print(decoded_jwt_token)
            # except:
            # print('토큰 낫유효')
            # return False
            decoded_id = decoded_jwt_token.get('id')
            if (decoded_id == obj.pk):
                return True
            else:
                print('토큰 불일치')
                return False  # Response({'msg': '잘못된 토큰입니다.'}, status=status.HTTP_403_FORBIDDEN)
