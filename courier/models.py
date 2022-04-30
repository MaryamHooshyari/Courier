from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=256, unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
