from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        "Email", unique=True, validators=[EmailValidator]
    )
    username = models.CharField(
        "Username", max_length=15, blank=True, null=True, unique=True
    )
    first_name = models.CharField(
        "First Name", max_length=25, blank=True, null=True
    )
    last_name = models.CharField(
        "Last Name", max_length=25, blank=True, null=True
    )
    profile_photo = models.URLField("Avatar", blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    # email field
    EMAIL_FIELD = "email"
    # unique field for each user
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
