from django.contrib import admin

from .models import Article, ContactMessage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at", "updated_at")
    list_editable = ("published",)
    list_filter = ("published", "created_at")
    search_fields = ("title", "summary", "body")
    date_hierarchy = "created_at"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "short_message", "is_read", "created_at")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")
    date_hierarchy = "created_at"
    actions = ["mark_read", "mark_unread"]

    def has_add_permission(self, request):
        return False

    def short_message(self, obj):
        return obj.message[:60] + ("…" if len(obj.message) > 60 else "")
    short_message.short_description = "پیام"

    @admin.action(description="علامت‌گذاری به‌عنوان خوانده‌شده")
    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="علامت‌گذاری به‌عنوان خوانده‌نشده")
    def mark_unread(self, request, queryset):
        queryset.update(is_read=False)
