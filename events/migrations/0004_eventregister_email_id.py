# Generated by Django 2.2.5 on 2019-09-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190907_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregister',
            name='email_id',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
