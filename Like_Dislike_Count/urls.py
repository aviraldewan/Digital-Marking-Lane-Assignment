from django.urls import path
from . import views

app_name = "Like_Dislike_Counter"
urlpatterns = [
    path("", views.index, name="index"),

    # API routes
    path("<str:count>", views.get_count, name="get_count"),
]
