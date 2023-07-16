from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    