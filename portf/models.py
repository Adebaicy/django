from django.db import models
#models is used when you wanna do less coding....building a ready made structure
# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=10)
    bio=models.CharField(max_length=500)
    img=models.ImageField(upload_to="portf/img")
    url=models.URLField(blank=True)    