from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    def __str__(self):
        return self.title