from rest_framework import serializers

from user.models import Teacher


class TeacherSettingsSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='account.email', read_only=True)
    faculty_name = serializers.CharField(source='faculty.name', read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"
        extra_kwargs = {
            'faculty': {'read_only': True}
        }
