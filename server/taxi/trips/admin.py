from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User

# alternative to admin.site.register(className) - use decorators
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass