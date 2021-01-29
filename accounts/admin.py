import csv
from django.contrib import admin
from django.http import HttpResponse
from accounts.models import User, Profile
from django.utils.html import format_html
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

class ExportCSVMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected users"

class UserAdmin(CustomUserAdmin, ExportCSVMixin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Information'), {'fields': ('first_name', 'last_name', 'section')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}), # 'groups'
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    list_display = ('email', 'first_name', 'last_name', 'section', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'section')
    search_fields = ('email', 'first_name', 'last_name', 'section')
    ordering = ('id', 'email')
    actions = ["export_as_csv"]

class ProfileAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="42" width="42"/>'.format(obj.image.url))
    
    ordering = ('id',)
    search_fields = ('user', 'id')
    list_filter = ('user',)
    list_display = ('user', 'image')
    image_tag.short_description = 'Image'

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)