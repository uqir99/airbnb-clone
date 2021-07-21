from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    

    """ Custom User Admin """

    list_display = ("username", "gender", "email", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")