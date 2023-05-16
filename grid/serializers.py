from rest_framework import serializers

from grid.models import Grid
from grid.utils import find_closest


class GridSerializer(serializers.ModelSerializer):
    default_error_messages = []
    data = serializers.RegexField(r"^(?:\-{0,1}\d+,\-{0,1}\d+;{0,1})+$", required=True)

    class Meta:
        model = Grid
        fields = "__all__"
        read_only_fields = ["created_at", "closest"]

    def create(self, validated_data):
        points = validated_data["data"].rstrip(";")
        validated_data["closest"] = find_closest(points)
        return super().create(validated_data)
