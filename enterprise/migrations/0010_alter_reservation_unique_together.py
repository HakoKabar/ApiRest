# Generated by Django 3.2.8 on 2021-10-10 20:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0009_alter_reservation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('Reseve_Par', 'Nom_Client')},
        ),
    ]
