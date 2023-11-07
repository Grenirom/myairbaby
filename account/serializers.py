from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from donor.serializers import DonorForReprSerializer
from surrogacy.serializers import SurrogacyForReprSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['surrogacy_applications'] = SurrogacyForReprSerializer(instance.surrogacy_applications.all(), many=True).data
        representation['donor_applications'] = DonorForReprSerializer(instance.donor_applications.all(), many=True).data
        return representation


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=129, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=129, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs.pop('password2')
        if password2 != password:
            raise serializers.ValidationError('Пароли не совпали!')
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'last_login', 'is_superuser', 'is_allowed', 'password')
