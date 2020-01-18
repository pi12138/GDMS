from django.db import models
# Create your models here.


class Faculty(models.Model):
    """
    学院模型
    """
    name = models.CharField(max_length=30, verbose_name="学院名", unique=True)
    number = models.CharField(max_length=30, verbose_name="学院编号", unique=True)
    monitor = models.CharField(max_length=30, verbose_name="院长")


class Profession(models.Model):
    """
    专业模型
    """
    name = models.CharField(max_length=30, verbose_name="专业名称", unique=True)
    number = models.CharField(max_length=30, verbose_name="专业编号", unique=True)


class Direction(models.Model):
    """
    方向模型
    """
    name = models.CharField(max_length=30, verbose_name="方向名称", unique=True)
    number = models.CharField(max_length=30, verbose_name="方向编号", unique=True)


class Klass(models.Model):
    """
    班级模型
    """
    name = models.CharField(max_length=30, verbose_name="班级名称", unique=True)
    number = models.CharField(max_length=30, verbose_name="班级编号", unique=True)


class Office(models.Model):
    """
    教研室模型
    """
    name = models.CharField(max_length=30, verbose_name="教研室名称", unique=True)
    number = models.CharField(max_length=30, verbose_name="教研室编号", unique=True)
