from django.db import models


class BD2(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title