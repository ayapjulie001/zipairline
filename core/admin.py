from django.contrib import admin
from .models import Airplane


class AirplaneAdmin(admin.ModelAdmin):
    search_fields = [
        'airplane',
    ]

    list_display = (
        'airplane',
        'id'
    )      

# Register your models here.


admin.site.register(Airplane, AirplaneAdmin)
