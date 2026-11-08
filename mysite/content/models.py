from django.db import models


class Article(models.Model):
    title = models.CharField("عنوان", max_length=200)
    summary = models.CharField("خلاصه", max_length=300)
    body = models.TextField("متن کامل مقاله")
    published = models.BooleanField("منتشر شود", default=True)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("آخرین ویرایش", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله‌ها"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField("نام فرستنده", max_length=100)
    email = models.EmailField("ایمیل")
    message = models.TextField("متن پیام")
    is_read = models.BooleanField("خوانده شده", default=False)
    created_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} ({self.email})"
