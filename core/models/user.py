from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# can create user and superuser
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        # email必須
        if not email:
            raise ValueError('Email address is must')

        user = self.model(
            email=self.normalize_email(email), # 大文字は小文字に変換
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    # オーバーライド
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        # 各種権限
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# model
class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # create instance
    objects = UserManager()

    # デフォルトではusernameとpasswordで認証
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name
