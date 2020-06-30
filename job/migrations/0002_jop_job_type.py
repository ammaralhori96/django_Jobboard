# Generated by Django 3.0.7 on 2020-06-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', '')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
