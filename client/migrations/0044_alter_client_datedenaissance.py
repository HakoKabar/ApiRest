# Generated by Django 3.2.8 on 2021-10-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0043_alter_client_datedenaissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
