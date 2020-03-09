from django.db import models

# Create your models here.
from subject.models import Subject


class GraduationDesign(models.Model):
    """
    毕业设计模型
    """
    subject = models.OneToOneField(verbose_name="课题", to=Subject, on_delete=models.CASCADE)
    design = models.FileField(verbose_name='毕业设计文件', upload_to="design/", blank=True, null=True)
    upload_time = models.DateTimeField(verbose_name="上传时间", blank=True, null=True)
    review_option = models.TextField(verbose_name="指导老师审核意见")
    review_time = models.DateTimeField(verbose_name="审阅时间", blank=True, null=True)

    def __str__(self):
        return "{}的毕业设计文件".format(self.subject)


class GraduationThesis(models.Model):
    """
    毕业论文模型
    """
    subject = models.OneToOneField(verbose_name="课题", to=Subject, on_delete=models.CASCADE)
    key_words = models.CharField(verbose_name="关键词", max_length=250)
    summary = models.TextField(verbose_name="摘要")
    thesis = models.FileField(verbose_name="毕业论文文件", upload_to="thesis/", blank=True, null=True)
    upload_time = models.DateTimeField(verbose_name="上传时间", blank=True, null=True)
    review_option = models.TextField(verbose_name="指导老师审核意见")
    review_time = models.DateTimeField(verbose_name="审阅时间", blank=True, null=True)

    def __str__(self):
        return "{}的毕业论文".format(self.subject)
