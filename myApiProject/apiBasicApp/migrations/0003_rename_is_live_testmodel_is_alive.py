# Generated by Django 3.2.3 on 2021-05-28 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiBasicApp', '0002_testmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='is_live',
            new_name='is_alive',
        ),
    ]
