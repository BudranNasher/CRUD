from django.urls import path
from .views import std_show, std_details

urlpatterns = [
    path('', std_show.as_view()),
    path('<int:pk>/', std_details.as_view()),
]