# type:ignore

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        # https://www.youtube.com/watch?v=iIsLwz_vkzA&ab_channel=Ot%C3%A1vioMiranda
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        blank=True,
        null=True
        )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True,
        null=True
        )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

