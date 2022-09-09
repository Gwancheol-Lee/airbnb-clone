from django.contrib import admin
from users import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """admin 패널 display 필드값 추가"""

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
