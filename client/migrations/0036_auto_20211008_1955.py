# Generated by Django 3.2.8 on 2021-10-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0035_alter_client_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateTimeField(default=1970),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
