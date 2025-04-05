from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    author = models.CharField(max_length=50, default="Unknown Author")
    availability=models.IntegerField(default=0)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title