# Generated by Django 3.2.4 on 2022-08-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='category',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='hscno',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='mail_id',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='mother_name',
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cat',
            field=models.CharField(choices=[('BC-A', 'BC-A'), ('BC-B', 'BC-B'), ('BC-D', 'BC-D'), ('BC-E', 'BC-E'), ('OC', 'OC'), ('SC', 'SC'), ('ST', 'ST')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cls10',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cls6',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cls7',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cls8',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='cls9',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='fathername',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='hsno',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='mothername',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='paymentID',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='ph',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=None, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='photo',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref1',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref2',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref3',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref4',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref5',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='pref6',
            field=models.CharField(choices=[('MPC', 'MPC'), ('BIPC', 'BIPC'), ('CEC', 'CEC'), ('HEC', 'HEC'), ('VOC', 'VOCATIONAL'), ('CHE', 'CHEMICAL')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='school',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='sign',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='studentname',
            field=models.CharField(default=None, max_length=70),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='username',
            field=models.CharField(default=None, max_length=16),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='aadhaar',
            field=models.CharField(default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='address',
            field=models.TextField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='alt_mobile',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='bankac',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='bankifsc',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='birth_district',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='birth_state',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='castecert',
            field=models.CharField(default=None, max_length=14, null=True),
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
            name='ewscert',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='hallticket',
            field=models.CharField(default=None, max_length=12),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='income',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='incomecert',
            field=models.CharField(default=None, max_length=14, null=True),
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
            name='pincode',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='ration',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='town',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='village',
            field=models.CharField(default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='yop',
            field=models.CharField(default=None, max_length=4, null=True),
        ),
    ]
