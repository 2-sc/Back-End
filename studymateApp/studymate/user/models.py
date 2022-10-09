from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password, **extra_fields):
        if not email:
            raise ValueError('이메일이 필요합니다.')
        if not nickname:
            raise ValueError('닉네임이 필요합니다.')
        user = self.model(
            email = self.normalize_email(email), # normalize_email -> 이메일의 대소문자 구분 없이 저장
            nickname = nickname,
            **extra_fields
        )
        self.is_staff = False
        user.set_password(password) # set_password -> 비밀번호를 암호화 시켜줌
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password, **extra_fields):
        super_user = self.create_user(email, nickname, password, **extra_fields)
        
        super_user.is_admin = True
        super_user.save(using=self._db)
        return super_user
        
class User(AbstractBaseUser):
    email = models.EmailField(max_length=128, verbose_name='이메일', unique=True)
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    image = models.ImageField(upload_to='profile/', default='default.jpeg', verbose_name='이미지')
    info = models.TextField(default='자기소개를 입력해주세요.' ,verbose_name='자기소개')
    # d_day = models.DateField(verbose_name='디데이')

    # User 모델의 필수 필드
    is_active = models.BooleanField(default=True)   
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    objects = UserManager()

    USERNAME_FIELD = 'email' # username 을 대신할 필드 설정
    REQUIRED_FIELDS = ['nickname'] # 필수로 작성해야 하는 필드 설정

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin
