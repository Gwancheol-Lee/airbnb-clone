from django.contrib import admin
from rooms import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass
