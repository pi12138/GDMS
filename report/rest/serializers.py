from rest_framework import serializers

from report.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        extra_kwargs = {
            'submit_time': {'format': "%Y-%m-%d %H:%M:%S"},
            'review_time': {"format": "%Y-%m-%d %H:%M:%S"}
        }
