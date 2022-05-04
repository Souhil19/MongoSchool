from django.shortcuts import render
from rest_framework import viewsets

from studentApp.models import Student
from studentApp.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer