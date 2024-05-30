from django.db import models

# Create your models here.

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    content = models.TextField(blank=False, null=False, default='')
    dateCreated = models.DateTimeField(auto_now=True, null=False)
