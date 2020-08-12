# Generated by Django 3.1 on 2020-08-12 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
        ('posts', '0002_auto_20200812_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='drinks.drinks'),
        ),
    ]
