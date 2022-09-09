from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """기존 장고 admin fieldsets + custom fieldsets 추가"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
