# Generated by Django 5.0 on 2023-10-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed',
            name='item_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='nonfixed',
            name='item_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]