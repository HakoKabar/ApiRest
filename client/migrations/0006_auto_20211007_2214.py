# Generated by Django 3.2.8 on 2021-10-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_reservation_typedecamion'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='DateDeNaissance',
            field=models.DateField(default='01/01/2021'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]