# Generated by Django 3.2.9 on 2021-11-25 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='how_did_you_sleep',
            new_name='How_did_you_sleep',
        ),
    ]