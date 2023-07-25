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

STATUS_CHOICES= (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length= 1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHIOCES, max_length=2)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year = models.DateField()
    views = models.IntegerField(default=0)