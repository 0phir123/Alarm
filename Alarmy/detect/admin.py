from django.contrib import admin
from .models import Detect
# Register your models here.
class DetectAdmin(admin.ModelAdmin):
    list_display = ('id', 'time')
    list_display_links = ('id','time')
    search_fields = ('time',)
    list_per_page = 25

admin.site.register(Detect, DetectAdmin)