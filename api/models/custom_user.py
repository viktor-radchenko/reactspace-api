from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email field'), unique=True)
    username = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username', 'first_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
