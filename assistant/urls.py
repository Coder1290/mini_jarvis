from django.urls import path
from .views import command_view, index

urlpatterns = [
    path("command/", command_view, name="command"),
    path("", index, name="index"),
    path("command/", command_view, name="command"),
]