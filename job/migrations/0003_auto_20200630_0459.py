# Generated by Django 3.0.7 on 2020-06-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jop_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jop',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15),
        ),
    ]
