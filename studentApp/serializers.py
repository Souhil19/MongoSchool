from rest_framework import serializers
from .models import Student, Subscription


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subscription
        fields='__all__'