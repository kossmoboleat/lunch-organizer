from lunch.models import Lunch
from django.contrib import admin

class LunchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lunch, LunchAdmin)