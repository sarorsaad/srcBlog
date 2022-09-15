from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
   

    # Fields
    title = models.CharField(max_length=30)
    
    content = models.TextField(max_length=100)
   
    
    image = models.ImageField(upload_to="post-images/")

    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("post_update", args=(self.pk,))