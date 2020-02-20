from django.db import models

# Create your models here.
from user.models import Teacher, Student, Administrator


class Subject(models.Model):
    """
    课题模型
    """
    REVIEW_RESULT_VALUE = (
        (0, "待审核"),
        (1, "审核通过"),
        (2, "审核未通过")
    )

    subject_name = models.CharField(verbose_name="课题名称", max_length=100)
    questioner = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, verbose_name="出题人")
    number_of_people = models.IntegerField(verbose_name="课题人数", default=1)
    select_student = models.ForeignKey(to=Student, on_delete=models.CASCADE, verbose_name="选题学生")
    subject_description = models.TextField(verbose_name="课题描述")
    expected_goal = models.TextField(verbose_name="预期目标")
    require = models.TextField(verbose_name="对学生知识和能力的要求")
    required_conditions = models.TextField(verbose_name="所需条件")
    references = models.TextField(verbose_name="参考资料")
    declare_time = models.DateTimeField(verbose_name="申报时间", auto_now=True,)
    reviewer = models.ForeignKey(Administrator, on_delete=models.CASCADE, verbose_name="审核人")
    review_result = models.IntegerField(choices=REVIEW_RESULT_VALUE, default=0, verbose_name="审核结果")
    review_time = models.DateTimeField(verbose_name="审核时间", auto_now=True)

    def __str__(self):
        return self.subject_name
