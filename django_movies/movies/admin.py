from django.contrib import admin
from .models import Movie, Rater, Ratings

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rater)
admin.site.register(Ratings)
