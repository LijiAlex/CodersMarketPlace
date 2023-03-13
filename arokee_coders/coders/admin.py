from django.contrib import admin
from .models import Coder

# Register your models here.

class CoderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hourly_rate', 'category', 'type', 'is_featured')
    list_display_links = ('id', 'name' )
    search_fields = ('category', 'name')
    list_filter = ('is_featured','category')
    list_editable = ('is_featured',)


admin.site.register(Coder, CoderAdmin)