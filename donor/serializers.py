from rest_framework import serializers
from .models import DonorApplication


class DonorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        exclude = ('special_code', )
