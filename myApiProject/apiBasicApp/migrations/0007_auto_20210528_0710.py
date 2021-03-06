# Generated by Django 3.2.3 on 2021-05-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiBasicApp', '0006_auto_20210528_0637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Test Model'},
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TestContent', to='apiBasicApp.testmodel')),
            ],
            options={
                'verbose_name_plural': 'Model X',
            },
        ),
    ]
