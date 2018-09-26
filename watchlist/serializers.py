from rest_framework import serializers
from .models import DwDowjRecordIndex


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DwDowjRecordIndex
        fields = ('id', 'record_id', 'record_name', 'id_type', 'id_value')


class IdentifyResultResponseData(serializers.Serializer):
    record_name = serializers.CharField(required=True, allow_blank=True),
    id_type = serializers.CharField(required=True, allow_blank=True),
    id_value = serializers.CharField(required=True, allow_blank=True),
    result = serializers.CharField(required=True, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class IdentifyResultSerializer(serializers.Serializer):  # 它序列化的方式很类似于Django的forms

    return_code = serializers.CharField(required=True, allow_blank=True)
    return_info = serializers.CharField(required=True, allow_blank=True)
    # rsp_data = IdentifyResultResponseData(required=True)True
    rsp_data = serializers.JSONField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
