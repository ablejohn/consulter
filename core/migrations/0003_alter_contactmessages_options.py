# Generated by Django 4.2.13 on 2024-05-24 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactmessages_alter_ourservices_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmessages',
            options={'verbose_name': 'Contact Message', 'verbose_name_plural': 'Contact Messages'},
        ),
    ]