from django.db import models

# Create your models here.
class Movie(models.Model):
    Name=models.CharField(max_length=50)
    Des=models.TextField()
    Year=models.IntegerField()
    Img=models.ImageField(upload_to= 'gallery',default="00")

    def __str__(self):
        return self.Name