from django.db import models
from django.contrib.auth.models import User


class URLs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    orig_url = models.CharField(max_length=100)
    short_url = models.CharField(max_length=50, unique=True)
    views = models.IntegerField(default=0, verbose_name='Views')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['-created_at']
