from rest_framework import serializers
from .models import Property
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer


class PropertySerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('__all__')
        list_serializer_class = BulkListSerializer

    def create(self, validated_data):
        obj = Property.objects.create(**validated_data)
        return obj


