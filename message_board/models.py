from django.db import models

# Create your models here.
from user.models import Student, Teacher


class MessageBoard(models.Model):
    """
    留言板模型
    """
    title = models.CharField(verbose_name="标题", max_length=100, blank=True, null=True)
    content = models.TextField(verbose_name="主要内容", blankl=True, null=True)
    annex = models.FileField(verbose_name="附件", upload_to='message/', blank=True, null=True)
    publish_time = models.DateTimeField(verbose_name="发表时间", blank=True, null=True)
    publisher = models.ForeignKey(verbose_name="发表人", to=Student, on_delete=models.CASCADE)
    receiver = models.ForeignKey(verbose_name="接收人", to=Teacher, on_delete=models.CASCADE)
    is_read = models.BooleanField(verboose_name="是否已读", default=False)

    def __str__(self):
        return self.title
