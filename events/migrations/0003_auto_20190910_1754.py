# Generated by Django 2.2.5 on 2019-09-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190910_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='eventregister',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
    ]