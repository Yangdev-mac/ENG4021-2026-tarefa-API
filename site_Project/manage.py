from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.catalogo, name="catalogo"),
]
