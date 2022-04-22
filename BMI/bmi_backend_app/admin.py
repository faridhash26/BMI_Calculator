from django.contrib import admin
from .models import UserBmiInfo
# Register your models here.
@admin.register(UserBmiInfo)
class UserBmiInfo(admin.ModelAdmin):
    list_display = ("id",  'age', "height" ,"weight","bmi" ,"status")
