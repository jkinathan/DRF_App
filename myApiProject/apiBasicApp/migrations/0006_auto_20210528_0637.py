# Generated by Django 3.2.3 on 2021-05-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiBasicApp', '0005_auto_20210528_0621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='slug',
            field=models.CharField(default='null', editable=False, max_length=250),
        ),
    ]
