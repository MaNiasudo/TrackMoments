from django.contrib import admin
from .models import Integration, Activity, Books , Movies
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "read_data"]



admin.site.register(Integration)
admin.site.register(Activity)
admin.site.register(Books,BooksAdmin)
admin.site.register(Movies)