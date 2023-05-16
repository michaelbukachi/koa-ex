from django.db import models

# Create your models here.


class Grid(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=255)
    closest = models.CharField(max_length=255)
