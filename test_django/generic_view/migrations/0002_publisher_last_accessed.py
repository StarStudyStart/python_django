# Generated by Django 2.2.4 on 2020-03-06 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generic_view', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='last_accessed',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
