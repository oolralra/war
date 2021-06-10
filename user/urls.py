from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignView.as_view(), name='sign-up'),
]