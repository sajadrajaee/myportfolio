from django.db import models

# Create your models here.
class MyBlogs(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='mywebapp/images', default=None, null=True)
    
    def __str__(self):
        return self.title
    