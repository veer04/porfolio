# Generated by Django 4.0.3 on 2022-05-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veer', '0002_person_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(),
        ),
    ]
