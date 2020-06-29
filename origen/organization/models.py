from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Organization(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null= True, blank=True)
    description = models.TextField(max_length=255, default='', null=True, blank=True)
    color = models.CharField(max_length=7, default='#1B9A4B')
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(default=timezone.now, null=False)
   
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    