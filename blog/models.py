from django.db import models
#models is used when you wanna do less coding....building a ready made structure
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=10)
    des=models.CharField(max_length=500)
    def __str__(self):
        return self.title
       
