from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=True)
router.register(r"signup", views.SingUpViewSet, basename="siguup")

urlpatterns = [
    path("", include(router.urls)),
]
