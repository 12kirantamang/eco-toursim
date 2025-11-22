from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'message', 'created_at')  # columns to show
    list_filter = ('created_at',)  # filter sidebar by date
    search_fields = ('first_name', 'last_name', 'email', 'message')  # search bar
    ordering = ('-created_at',)  # newest first

# Register once
admin.site.register(Contact, ContactAdmin)
