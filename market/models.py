from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image = models.ImageField(upload_to='books/')
    DisplayFields = ['name', 'page_count', 'category', 'author_name', 'price']

    def __str__(self):
        return self.name
