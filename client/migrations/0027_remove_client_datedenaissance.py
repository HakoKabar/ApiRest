# Generated by Django 3.2.8 on 2021-10-08 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_client_datedenaissance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='DateDeNaissance',
        ),
    ]