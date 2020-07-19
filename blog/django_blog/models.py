from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    title = models.CharField(max_length = 150)
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)
    image = models.ImageField(null=True,blank=True,upload_to='images')
    slug = models.SlugField(blank = True)
    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-detail', kwargs={'slug': self.slug})

class Author(AbstractUser):
    
    created_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.first_name 