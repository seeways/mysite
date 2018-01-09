from django.db import models


# Create your models here.

class UserInfo(models.Model):  # 需要继承Model类
    # 创建两个char类型字段，最大长度为32
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
