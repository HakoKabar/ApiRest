# Generated by Django 3.2.8 on 2021-10-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0037_alter_client_datedenaissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Adress',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
