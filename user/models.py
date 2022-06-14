from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            email=email, #이메일 추가
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        # python manage.py createsuperuser 사용 시 해당 함수가 사용됨

    def create_superuser(self, username, password,email):
        user = self.create_user(
            username=username,
            password=password,
            email=email, #이메일 추가
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username=models.CharField("사용자이름",max_length=50,unique=True) #pk로 지정
    password=models.CharField("비밀번호",max_length=250)
    email=models.EmailField("이메일")
    nickname=models.CharField("닉네임",max_length=100)
    created_at=models.DateField("가입날짜",auto_now_add=True)
    is_active=models.BooleanField(default=True) #비활성화여부

    # is_staff에서 해당 값 사용
    is_admin = models.BooleanField(default=False)

    # createsuperuser로 로그인할때 USERNAME_FIELD에 지정한 필드와 password를 입력받겠다.
    # USERNAME_FIELD는 PK인 필드만 가능하다
    USERNAME_FIELD = 'username'

    # createsuperuser로 user를 생성할 때 입력받은 필드 지정(USERNAME_FIELD입력받은 필드, password 빼고)
    REQUIRED_FIELDS = ['email']

    #custom user생성 시 필요
    #username, email, password 로 입력받음
    objects = UserManager()

    def __str__(self):
        return self.username

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):
    user=models.OneToOneField(to=User,verbose_name="사용자",primary_key=True,on_delete=models.CASCADE)
    introduction=models.CharField("소개글",max_length=300)

    def __str__(self):
        return f"{self.user}의 프로필"



