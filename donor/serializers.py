from rest_framework import serializers
from .models import DonorApplication


class DonorRegisterSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = DonorApplication
        exclude = ('special_code', )


class DonorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        fields = '__all__'


class DonorListForAllowed(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        exclude = ('user', 'last_name', 'first_name', 'phone_number', 'photo_fas', 'photo_full', 'photo_side')


class DonorForReprSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        fields = ('id', 'special_code')


class DonorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorApplication
        exclude = ('id', 'special_code', 'user')
