from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
    

class project(models.Model):
    title=models.CharField(max_length=200)
    link=models.URLField(blank=True ,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='project/', null=True,blank=True)
    priority=models.PositiveIntegerField(default=1)

    tags=models.ManyToManyField(
        Tag, blank=True,related_name='projects'
    )

    class Meta:
        ordering=['priority']

    def __str__(self):
        return self.title
