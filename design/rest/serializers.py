from rest_framework import serializers

from design.models import GraduationDesign


class GraduationDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduationDesign
        fields = "__all__"

