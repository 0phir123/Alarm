from django.contrib import admin

# Register your models here.

from .models import Database

class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'trigger', 'time')
    list_display_links = ('id','time')
    search_fields = ('time',)
    list_per_page = 25

admin.site.register(Database, DatabaseAdmin)


