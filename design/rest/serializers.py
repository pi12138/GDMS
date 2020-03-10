from rest_framework import serializers

from design.models import GraduationDesign


class GraduationDesignSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)
    filename = serializers.SerializerMethodField(method_name='get_filename', read_only=True)

    def get_filename(self, obj):
        if obj.design:
            filepath = obj.design.name
            return filepath.split('/')[-1]

        return None

    class Meta:
        model = GraduationDesign
        fields = "__all__"
        extra_kwargs = {
            'upload_time': {'format': "%Y-%m-%d %H:%M:%S"},
            'review_time': {'format': "%Y-%m-%d %H:%M:%S"},
        }

