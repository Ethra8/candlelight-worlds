from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class World(models.Model):
    
    display_name = models.CharField(max_length=100, null=False, blank=False, default='noname')
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField(default='noname')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_dining = CloudinaryField('image', null=True, blank=True)
    image_jakuzzi = CloudinaryField('image', null=True, blank=True)
    image_siesta = CloudinaryField('image', null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.display_name}'