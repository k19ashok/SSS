# Generated by Django 3.2.4 on 2022-08-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSS', '0004_auto_20220824_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='dob',
            field=models.DateField(default=None, null=True),
        ),
    ]
