# Generated by Django 3.2.8 on 2021-10-07 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_client_datedenaissance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='DateDeNaissance',
        ),
    ]
