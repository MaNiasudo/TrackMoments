from django.contrib import admin
from .models import Integration, Activity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_type", "created_at")
    list_filter = ("activity_type",)
    ordering = ("-created_at",)

admin.site.register(Integration)
admin.site.register(Activity,ActivityAdmin)
