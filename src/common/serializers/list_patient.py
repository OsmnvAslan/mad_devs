from rest_framework import serializers

from common.models import ExtendedUser


class ListPatient(serializers.ModelSerializer):
    diagnoses = serializers.StringRelatedField(many=True)

    class Meta:
        model = ExtendedUser
        fields = ('id', 'date_of_birth', 'diagnoses', 'created_at')
