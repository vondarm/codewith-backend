from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email=None, username=None, password=None, **other):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email) if email else None
        user = self.model(
            email=email,
            username=username,
            **other
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_anonymous(self, display_name):
        user = self.model(
            display_name=display_name
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(email=email, username=username, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    display_name = models.CharField(max_length=150, blank=True)
    is_anonymous_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.display_name or self.username or self.email or "Anonymous"
