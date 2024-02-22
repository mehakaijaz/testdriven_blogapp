from django.db import models
from django.urls  import reverse
from django.contrib.auth import get_user_model
# Create your models here.

""" 
class post
id =int
title=varchar
body=text
created at=date/time
updated at/modified at=date/time

"""
User=get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'id':self.pk})