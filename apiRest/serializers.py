from rest_framework import serializers
from .models import data

class DataSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    start = serializers.IntegerField()
    end = serializers.IntegerField()
    iri = serializers.DecimalField(max_digits = 10, decimal_places=10)

    def create(self, validate_data):
        instance = data()
        instance.start = validate_data.get('start')
        instance.end = validate_data.get('end')
        instance.iri = validate_data.get('iri')
        instance.save()
        return instance