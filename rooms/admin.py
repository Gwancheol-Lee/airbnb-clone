from django.contrib import admin
from rooms import models

@admin.register(models.RoomType, models.Facility, models.Amenity,  models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass
