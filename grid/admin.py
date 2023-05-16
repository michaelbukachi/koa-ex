from django.contrib import admin

from grid.models import Grid


# Register your models here.


@admin.register(Grid)
class GridAdmin(admin.ModelAdmin):
    list_display = ["created_at", "data", "closest"]
