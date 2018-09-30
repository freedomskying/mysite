from django.contrib import admin

# Register your models here.
from myrestaurants.models import Restaurant, Dish, Review, RestaurantReview

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)
