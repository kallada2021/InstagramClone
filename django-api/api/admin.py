"""Django Admin Customization"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from api import models


# TODO: Add fields to the Admin display fieldsets
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display: tuple = ["email", "username"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    # TODO: add remaining fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
