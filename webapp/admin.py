from django.contrib import admin
from .models import tweettable

@admin.register(tweettable)
class AdminTweettable(admin.ModelAdmin):

    list_display = ['user','is_liked','created_date','modified_date']

