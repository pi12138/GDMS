from rest_framework import serializers

from subject.models import Subject, ApplySubject
from user.models import Student


class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='questioner.name', read_only=True)
    teacher_phone = serializers.CharField(source='questioner.phone', read_only=True)
    teacher_qq = serializers.CharField(source='questioner.qq', read_only=True)
    teacher_email = serializers.CharField(source='questioner.account.email', read_only=True)
    office_name = serializers.CharField(source='questioner.office.name', read_only=True)
    student_name = serializers.SerializerMethodField(method_name="get_student")
    review_result = serializers.SerializerMethodField(method_name='get_review_result')
    reviewer_name = serializers.SerializerMethodField(method_name='get_reviewer_name')
    review_result_number = serializers.IntegerField(source='review_result')
    apply_student = serializers.SerializerMethodField(method_name='get_apply_student')

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

    def get_apply_student(self, obj):
        if hasattr(obj, 'applysubject_set'):
            query_set = obj.applysubject_set.order_by('-apply_time')
            if not query_set.exists():
                return None
            else:
                latest_apply = query_set[0]
                return latest_apply.student.name
        else:
            return None

    class Meta:
        model = Subject
        fields = "__all__"
        extra_kwargs = {
            'questioner': {'read_only': True},
            'declare_time': {'format': "%Y-%m-%d %H:%M:%S", 'read_only': True},
            'select_student': {'read_only': True}
        }


class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'subject_name', 'number_of_people')


class ApplySubjectSerializer(serializers.ModelSerializer):
    subject_info = SubjectInfoSerializer(source='subject', read_only=True)
    student_info = serializers.SerializerMethodField(method_name='get_student_info', read_only=True)

    def get_student_info(self, obj):
        if obj.student is None:
            return ""
        else:
            stu = obj.student
            info = {
                'name': stu.name,
                'qq': stu.qq,
                'phone': stu.phone
            }
            return info

    class Meta:
        model = ApplySubject
        fields = "__all__"
        extra_kwargs = {
            'apply_time': {'format': "%Y-%m-%d %H:%M:%S", 'read_only': True},
        }


