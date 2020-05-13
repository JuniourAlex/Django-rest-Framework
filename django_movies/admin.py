from django.contrib import admin
from .models import Actor, Genre, Movies, Rating, Reviews, RatingStar, Category

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(RatingStar)
