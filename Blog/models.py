from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    link=models.URLField(blank=True ,null=True)
    description=models.TextField()
    image=CloudinaryField('blog', null=True,blank=True)
    priority=models.PositiveIntegerField(default=1)

    class Meta:
        ordering=['priority']

    def __str__(self):
        return self.title