from django.db import models

# Create your models here.

from django.utils import timezone
from datetime import timedelta

class EmailVerificationCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        """判断验证码是否过期"""
        if self.created_at is None:
            return True  # 如果 created_at 为空，认为验证码已过期
        return timezone.now() > self.created_at + timedelta(seconds=61)
