from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "fav_book_genre",
                    "fav_movie_genre",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )

    list_filter = (
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )
