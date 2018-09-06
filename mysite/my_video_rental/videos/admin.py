from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title','length']
    search_fields = ['title']
    list_filter = ['release_year','length']
    list_display = ['title','release_year','length']
    list_editable = ['length']

class BookAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title','author']
    search_fields = ['title']
    list_filter = ['release_year','author']
    list_display = ['title','release_year','author']
    list_editable = ['author']
class CustomerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name','phone']
    search_fields = ['phone']
    list_filter = ['first_name','last_name']
    list_display = ['first_name','last_name','phone']
    list_editable = ['phone']
admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Book,BookAdmin)
