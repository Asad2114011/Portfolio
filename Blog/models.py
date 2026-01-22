from django.db import models
from project.models import Tag
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='blog/',blank=True,null=True)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    tags=models.ManyToManyField(
        Tag,related_name='blogs',blank=True
    )
    
    def __str__(self):
        return self.title

