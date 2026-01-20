from django.db import models

# Create your models here.
class cp(models.Model):
    title=models.CharField(max_length=50)
    link=models.URLField(null=True)
    image_url=models.URLField(null=True)
    description=models.TextField()
    rank=models.CharField(max_length=50,null=True)
    rating=models.CharField(max_length=50,null=True)
    solve=models.CharField(max_length=50,null=True)
    contest=models.CharField(max_length=50,null=True)
    priority=models.PositiveIntegerField(default=1)

    class Meta:
        ordering=['priority']

    def __str__(self):
        return self.title