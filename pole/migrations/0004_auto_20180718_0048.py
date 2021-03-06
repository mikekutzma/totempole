# Generated by Django 2.0.7 on 2018-07-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pole', '0003_change_creation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['ranking']},
        ),
        migrations.AlterField(
            model_name='change',
            name='from_rank',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='change',
            name='to_rank',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='ranking',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
