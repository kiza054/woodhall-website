import csv
from taggit.models import Tag
from django.contrib import admin
from django.http import HttpResponse
from taggit_helpers.admin import TaggitStackedInline
from main_website.models import Article, Event, ImageGallery, ImageGalleryCategory, WaitingList, UrgentAnnouncements

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

    export_as_csv.short_description = "Export selected Waiting List Entries"

class EventAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('title',)
    list_filter = ('start_time', 'end_time')
    list_display = (
        'title', 
        'description', 
        'start_time', 
        'end_time' 
    )

class ArticleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('article_name', 'id')
    list_filter = ('status',)
    list_display = (
        'article_name', 
        'author', 
        'date_posted', 
        'updated_on',
        'status'
    )
    exclude = ('tags',)
    inlines = [TaggitStackedInline]
    date_hierarchy = 'date_posted'

class WaitingListAdmin(admin.ModelAdmin, ExportCSVMixin):
    verbose_name = 'Waiting List'
    ordering = ('id',)
    search_fields = ('section_of_interest', 'id')
    list_filter = ('section_of_interest',)
    list_display = (
        'first_name', 
        'last_name', 
        'date_of_birth', 
        'section_of_interest', 
        'name_of_parent_carer', 
        'parent_carer_email', 
        'parent_carer_phone_number', 
        'parent_carer_address', 
        'date_of_submission'
    )
    actions = ["export_as_csv"]

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')

class ImageGalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(UrgentAnnouncements)
admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(WaitingList, WaitingListAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(ImageGalleryCategory, ImageGalleryCategoryAdmin)