# Generated by Django 3.1 on 2020-08-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_auto_20200813_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
