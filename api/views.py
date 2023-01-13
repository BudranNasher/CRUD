from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer 


class students_list(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        student = self.request.query_params.get('student')
        return queryset

class student_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
