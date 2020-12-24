from django.urls import path, include
from library.router import router
from library import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("api/", include(router.urls)),
]