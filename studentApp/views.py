from django.shortcuts import render
from rest_framework import viewsets

from studentApp.models import Student, Subscription
from studentApp.serializers import StudentSerializer, SubSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


