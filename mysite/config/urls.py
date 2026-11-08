from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from content.views import article_detail, home

admin.site.site_header = "پنل مدیریت سایت"
admin.site.site_title = "پنل مدیریت"
admin.site.index_title = "خوش آمدید"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", home, name="home"),
    path("articles/<int:pk>/", article_detail, name="article_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
