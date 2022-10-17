from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display: tuple = ('firstname', 'lastname', 'location', 'username')

admin.site.register(Profile, ProfileAdmin)