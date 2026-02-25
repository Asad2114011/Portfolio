from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    link=models.URLField(blank=True ,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='blog/', null=True,blank=True)
    priority=models.PositiveIntegerField(default=1)

    class Meta:
        ordering=['priority']

    def __str__(self):
        return self.title