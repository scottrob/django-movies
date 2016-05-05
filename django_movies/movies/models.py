from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)

class Ratings(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()

class Rater(models.Model):
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.IntegerField(default=0)
