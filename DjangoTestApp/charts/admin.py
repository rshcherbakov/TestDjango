from django.contrib import admin
from .models import RatesToStore

class RatesToStoreAdmin(admin.ModelAdmin):
    fieldset = [("Курс",{'fields':['RatesToStore']})]

admin.site.register(RatesToStore)
