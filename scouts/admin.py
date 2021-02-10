from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from scouts.models import Post, Image, Comment, File

class PostImageInline(admin.StackedInline):
    model = Image
    extra = 3

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'author', 'status', 'date_posted', 'updated_on')
    list_filter = ('date_posted', 'updated_on', 'status')
    search_fields = ['title', 'content', 'post_tags']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_draft', 'make_published']
    inlines = [PostImageInline]

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='1')
        if rows_updated == 1:
            message_bit = "1 Post was"
        else:
            message_bit = "%s Posts were" % rows_updated
        self.message_user(request, "%s successfully marked as Published." % message_bit)

    make_published.short_description = "Mark selected Posts as Published"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='0')
        if rows_updated == 1:
            message_bit = "1 Post was"
        else:
            message_bit = "%s Posts were" % rows_updated
        self.message_user(request, "%s successfully marked as Draft." % message_bit)

    make_draft.short_description = "Mark selected Posts as Draft"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'date_posted', 'active')
    list_filter = ('active', 'date_posted')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'uploaded_at', 'file')

admin.site.register(Post, PostAdmin)
admin.site.register(File, FilesAdmin)
admin.site.register(Comment, CommentAdmin)