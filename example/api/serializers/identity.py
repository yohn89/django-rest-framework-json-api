from django.contrib.auth import models as auth_models
from rest_framework import serializers


class IdentitySerializer(serializers.ModelSerializer):
    """
    Identity Serializer
    """

    def add_meta(self, meta):
        return {'copyright': '2015'}

    class Meta:
        model = auth_models.User
        fields = (
            'id', 'first_name', 'last_name', 'email', )
