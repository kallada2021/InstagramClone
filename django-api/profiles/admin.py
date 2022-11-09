from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display: tuple = ("username", "email", "firstname", "id")


admin.site.register(Profile, ProfileAdmin)
