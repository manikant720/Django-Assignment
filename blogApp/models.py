
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blogImages', null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailPost', kwargs={'pk': self.pk})