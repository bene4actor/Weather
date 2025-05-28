from rest_framework import serializers


class CityStatsSerializer(serializers.Serializer):
    city_name = serializers.CharField()
    count = serializers.IntegerField()
