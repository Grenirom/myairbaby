from rest_framework import serializers
from .models import DonorApplication


class DonorRegisterSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = DonorApplication
        exclude = ('special_code', 'user_email')


class DonorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        fields = '__all__'


class DonorListForAllowed(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        exclude = ('user_email', 'last_name', 'first_name', 'phone_number')
