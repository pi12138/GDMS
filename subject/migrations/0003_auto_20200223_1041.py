# Generated by Django 2.2 on 2020-02-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20200221_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='review_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='审核时间'),
        ),
    ]
