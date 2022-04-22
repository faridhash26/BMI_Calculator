from django.contrib import admin

from .models import BMIUser
# Register your models here.
@admin.register(BMIUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', "email",  'is_staff', 'is_active', 'date_joined', )
