from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
   

    # Fields
    title = models.CharField(max_length=30)
    
    content = models.TextField(max_length=100)
   
    
    image = models.ImageField(upload_to="post-images/")

    class Meta:
        pass

    def __str__(self):
        return str(self.title)