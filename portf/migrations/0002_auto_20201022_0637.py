# Generated by Django 3.1.2 on 2020-10-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
