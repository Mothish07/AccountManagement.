# Generated by Django 4.2.6 on 2023-10-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_uploadfile_nonfixedamount_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedamount',
            name='upload_file',
            field=models.FileField(default='your_default_value', upload_to='uploads/'),
        ),
    ]
