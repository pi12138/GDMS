# Generated by Django 2.2 on 2020-02-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_administrator_name'),
        ('subject', '0004_subject_review_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='apply_students',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply_students', to='user.Student', verbose_name='申请学生'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='select_student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='select_student', to='user.Student', verbose_name='选题学生'),
        ),
    ]
