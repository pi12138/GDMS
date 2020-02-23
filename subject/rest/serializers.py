from rest_framework import serializers

from subject.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='questioner.name', read_only=True)
    office_name = serializers.CharField(source='questioner.office.name', read_only=True)
    student_name = serializers.SerializerMethodField(method_name="get_student")
    review_result = serializers.SerializerMethodField(method_name='get_review_result')
    reviewer_name = serializers.SerializerMethodField(method_name='get_reviewer_name')

    def get_student(self, obj):
        if not obj.select_student:
            return ""
        return obj.select_student.name

    def get_review_result(self, obj):
        return obj.get_review_result_display()

    def get_reviewer_name(self, obj):
        if not obj.reviewer:
            return ""
        return obj.reviewer.name

    class Meta:
        model = Subject
        fields = "__all__"
        extra_kwargs = {
            'questioner': {'read_only': True},
            'declare_time': {'format': "%Y-%m-%d %H:%M:%S", 'read_only': True},
            'review_time': {'format': "%Y-%m-%d %H:%M:%S", 'read_only': True},
            'select_student': {'read_only': True}
        }
