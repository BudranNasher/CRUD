from django.urls import path
from .views import students_list, student_details

urlpatterns = [
    path('', students_list.as_view()),
    path('<int:pk>/', student_details.as_view()),
]