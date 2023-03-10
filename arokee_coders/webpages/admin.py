from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, TeamMember

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    @admin.display(description='')
    def thePhoto(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" />')    

    @admin.display(description='Name')
    def theName(self, object):
        return (object.first_name +" "+ object.last_name)
    
    list_display = ('id','thePhoto', 'theName', 'role')
    list_display_links = ('theName', 'thePhoto' )
    search_fields = ('first_name', 'role')
    list_filter = ('role',)



admin.site.register(Banner)
admin.site.register(TeamMember, TeamAdmin)
