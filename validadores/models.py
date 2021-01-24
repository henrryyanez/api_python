from django.db import models

from django.conf import settings
 # Create Movie Model


class Validator(models.Model):
    #creator = models.ForeignKey('auth.User', related_name='validadores', on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='validadores', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cuota = models.IntegerField(default=0, blank=True)
    resto = models.IntegerField(default=0, blank=True)
    texto = models.CharField(db_column='texto', max_length=5000, blank=False)
    predict = models.CharField(max_length=50000, blank=True)
    is_member = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
