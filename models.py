from django.db import models



# Create your models here.

class List_book(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn=models.CharField(max_length=15)

    def __str__(self):
        return self.title