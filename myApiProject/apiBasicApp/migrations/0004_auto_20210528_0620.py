# Generated by Django 3.2.3 on 2021-05-28 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apiBasicApp', '0003_rename_is_live_testmodel_is_alive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ['name'], 'verbose_name': 'ModelName'},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
