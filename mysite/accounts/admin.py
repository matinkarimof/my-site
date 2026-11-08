from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from .forms import AdminChangeForm, RegisterForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = AdminChangeForm
    add_form = RegisterForm

    list_display = ("phone", "first_name", "last_name", "avatar_thumb", "is_staff", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone", "first_name", "last_name")
    ordering = ("-date_joined",)
    readonly_fields = ("avatar_preview", "last_login", "date_joined")

    fieldsets = (
        ("ورود", {"fields": ("phone", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name", "email", "avatar", "avatar_preview")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("تاریخ‌های مهم", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("phone", "first_name", "password1", "password2")}),
    )

    def avatar_thumb(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="36" height="36" style="border-radius:50%;object-fit:cover">',
                obj.avatar.url,
            )
        return "—"
    avatar_thumb.short_description = "تصویر"

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="140" height="140" style="border-radius:16px;object-fit:cover">',
                obj.avatar.url,
            )
        return "بدون تصویر"
    avatar_preview.short_description = "پیش‌نمایش"
