# Generated by Django 3.2.4 on 2022-08-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSS', '0002_auto_20220824_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='sub',
            field=models.BooleanField(default=False),
        ),
    ]
