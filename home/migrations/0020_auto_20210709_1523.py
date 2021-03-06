# Generated by Django 3.1.7 on 2021-07-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210704_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('mission_id', models.AutoField(primary_key=True, serialize=False)),
                ('mission_code', models.CharField(max_length=500)),
                ('mission_thumb1', models.ImageField(default='', upload_to='uploads/mission')),
                ('mission_thumb2', models.ImageField(default='', upload_to='uploads/mission')),
                ('mission_thumb3', models.ImageField(default='', upload_to='uploads/mission')),
                ('mission_title', models.CharField(max_length=500)),
                ('mission_date', models.DateField()),
                ('mission_location', models.CharField(max_length=500)),
                ('mission_YT_link', models.URLField()),
                ('mission_content', models.TextField(max_length=1000)),
                ('mission_lv', models.CharField(max_length=500)),
                ('mission_lv_link', models.URLField()),
                ('mission_payload', models.CharField(max_length=500)),
                ('mission_payload_link', models.URLField()),
                ('mission_link1_Name', models.CharField(max_length=500)),
                ('mission_link1', models.URLField()),
                ('mission_link2_Name', models.CharField(max_length=500)),
                ('mission_link2', models.URLField()),
                ('mission_link3_Name', models.CharField(max_length=500)),
                ('mission_link3', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='rocket',
            name='rocket_stage4_show',
            field=models.CharField(choices=[('block', 'block'), ('none', 'none')], max_length=10),
        ),
    ]
