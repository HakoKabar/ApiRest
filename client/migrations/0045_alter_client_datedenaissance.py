# Generated by Django 3.2.8 on 2021-10-09 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0044_alter_client_datedenaissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateField(default=datetime.datetime(2021, 10, 9, 11, 50, 52, 326328, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
