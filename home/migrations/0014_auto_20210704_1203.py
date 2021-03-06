# Generated by Django 3.1.7 on 2021-07-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rocket'),
    ]

    operations = [
        migrations.AddField(
            model_name='rocket',
            name='rocket_stage1_thumb',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='rocket',
            name='rocket_stage2_thumb',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='rocket',
            name='rocket_stage3_thumb',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='rocket',
            name='rocket_stage4_thumb',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='rocket',
            name='rocket_thumb',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]
