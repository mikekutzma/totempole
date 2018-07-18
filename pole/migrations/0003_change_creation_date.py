# Generated by Django 2.0.7 on 2018-07-18 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pole', '0002_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
    ]
