# Generated by Django 3.2.8 on 2021-10-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0032_client_datedenaissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]