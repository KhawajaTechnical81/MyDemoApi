from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register(r'Document', views.DocumentViewSet)
router.register(r'DocAttach', views.DocAttachViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
