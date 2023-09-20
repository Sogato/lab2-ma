from django.db import models


class BD1(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField(blank=True, default='')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title
