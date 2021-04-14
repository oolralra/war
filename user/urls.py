from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=True)
router.register(r"signup", views.SingUpViewSet, basename="v1")

urlpatterns = [
    path('api/', include(router.urls)),
    path('upload/', views.CsvUploadView.as_view(), name="upload"),
]
