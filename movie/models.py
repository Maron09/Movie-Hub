from django.db import models


CATEGORY_CHIOCES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)
LANGUAGE_CHOICES= (
    ('EN', 'ENGLISH'),
    ('GR', 'GERMAN'),
)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length= 1000)
    image = models.ImageField(upload='movies')
    category = models.CharField(choices=CATEGORY_CHIOCES, max_length=2)