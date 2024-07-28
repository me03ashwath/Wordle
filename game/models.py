from django.db import models
from django.contrib.auth.models import User

class Words(models.Model):
    word_length = models.IntegerField()
    word = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return self.word
    
    class Meta:
        verbose_name_plural = 'Words'
            