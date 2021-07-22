from django.db import models
#import django.contrib.postgres.fields as pg_fields
class  Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveSmallIntegerField(default=0)


class User(models.Model):
    pass