from django.contrib import admin
from django.urls import path, include

app_name = "blogicum"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("posts/", include("blog.urls")),
    path("category/", include("blog.urls")),
    path("pages/", include("pages.urls")),
]
