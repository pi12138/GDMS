# Generated by Django 2.2 on 2020-02-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200219_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='姓名'),
        ),
    ]
