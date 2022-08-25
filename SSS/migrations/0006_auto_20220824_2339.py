# Generated by Django 3.2.4 on 2022-08-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSS', '0005_auto_20220824_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='address',
            field=models.TextField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='cat',
            field=models.CharField(choices=[('BC-A', 'BC-A'), ('BC-B', 'BC-B'), ('BC-D', 'BC-D'), ('BC-E', 'BC-E'), ('OC', 'OC'), ('SC', 'SC'), ('ST', 'ST')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='dob',
            field=models.CharField(default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='ews',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=None, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='medium',
            field=models.CharField(choices=[('TELUGU', 'TELUGU'), ('TELUGU', 'TELUGU')], default=None, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='minority',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='ph',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=None, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref1',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref2',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref3',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref4',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref5',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='pref6',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
    ]