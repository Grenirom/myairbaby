from rest_framework import serializers

from surrogacy.models import Surrogacy


class SurrogacyCreateSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Surrogacy
        fields = '__all__'

