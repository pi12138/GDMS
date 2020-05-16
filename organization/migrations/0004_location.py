# Generated by Django 2.2 on 2020-04-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20200123_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_number', models.CharField(max_length=100, unique=True, verbose_name='地点代号')),
                ('location_desc', models.TextField(blank=True, null=True, verbose_name='地点详细信息描述')),
            ],
        ),
    ]