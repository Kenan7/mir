from django.contrib import admin
from core.models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ('name', 'email')
    readonly_fields = ['name', 'email', 'message', 'created_at']
    search_fields = ('name', 'email')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
