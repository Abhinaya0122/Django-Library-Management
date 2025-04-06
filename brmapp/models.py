from django.utils import timezone  
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    author = models.CharField(max_length=50, default="Unknown Author")
    availability=models.IntegerField(default=0)
    image_url = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.title
    
class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(default=timezone.now)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
