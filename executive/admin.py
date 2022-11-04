from django.contrib import admin

from executive.models import QuartermastersItemInventory


class QuartermastersItemInventoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('item_name', 'id')
    list_filter = ('category',)
    list_display = ('item_name', 'item_quantity', 'category', 'added_on', 'updated_on')

admin.site.register(QuartermastersItemInventory, QuartermastersItemInventoryAdmin)