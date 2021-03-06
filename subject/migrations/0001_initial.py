# Generated by Django 2.2 on 2020-02-20 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20200219_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100, verbose_name='课题名称')),
                ('number_of_people', models.IntegerField(default=1, verbose_name='课题人数')),
                ('subject_description', models.TextField(verbose_name='课题描述')),
                ('expected_goal', models.TextField(verbose_name='预期目标')),
                ('require', models.TextField(verbose_name='对学生知识和能力的要求')),
                ('required_conditions', models.TextField(verbose_name='所需条件')),
                ('references', models.TextField(verbose_name='参考资料')),
                ('declare_time', models.DateTimeField(auto_now=True, verbose_name='申报时间')),
                ('review_result', models.IntegerField(choices=[(0, '待审核'), (1, '审核通过'), (2, '审核未通过')], default=0, verbose_name='审核结果')),
                ('review_time', models.DateTimeField(auto_now=True, verbose_name='审核时间')),
                ('questioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Teacher', verbose_name='出题人')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Administrator', verbose_name='审核人')),
                ('select_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='选题学生')),
            ],
        ),
    ]
