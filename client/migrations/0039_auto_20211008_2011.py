# Generated by Django 3.2.8 on 2021-10-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0038_client_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Adress',
        ),
        migrations.AlterField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateField(auto_now=True),
        ),
    ]