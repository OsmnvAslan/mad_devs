# Generated by Django 3.1.5 on 2021-10-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='is_doctor',
            field=models.BooleanField(default=True),
        ),
    ]
