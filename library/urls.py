from django.urls import path, include
from .router import router
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("api/", include(router.urls)),
]