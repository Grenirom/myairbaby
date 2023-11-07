from rest_framework import serializers

from surrogacy.models import Surrogacy


class SurrogacyCreateSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Surrogacy
        exclude = ('special_code', )


class SurrogacyAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surrogacy
        fields = '__all__'


class SurrogacyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surrogacy
        exclude = ('special_code', 'owner_email')


class SurrogacyForReprSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surrogacy
        fields = ('id', 'special_code' )
