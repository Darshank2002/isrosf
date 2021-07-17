from django.db import models
from django.db.models.enums import Choices
import datetime


class MissionPost(models.Model):
    TYPE = [('leo', 'LEO'), ('geo', 'GEO'), ('interplanetary', 'Interplanetary'),
            ('human', 'Human-Spaceflight')]

    mission_id = models.AutoField(primary_key=True)
    mission_type = models.CharField(blank=True, max_length=50, choices=TYPE)
    mission_title = models.CharField(max_length=100)
    mission_site = models.CharField(max_length=100)
    mission_content = models.CharField(max_length=500)
    mission_date = models.DateField()
    post_thumbnail = models.ImageField(upload_to='', default="")

    def __str__(self):
        return self.mission_title


class Timeline(models.Model):
    # TYPE = [('left', 'left'), ('right', 'right')]
    event_id = models.AutoField(primary_key=True)
    # event_side = models.CharField(blank=True, max_length=50, choices=TYPE)

    event_title = models.CharField(max_length=100)
    event_content = models.CharField(max_length=500)
    event_link_content = models.CharField(max_length=100)
    event_link = models.URLField(max_length=200)

    def side(self):
        if (self.event_id % 2 == 0):
            return "left"
        else:
            return "right"

    def __str__(self):
        return self.event_title


class Mission(models.Model):
    TYPE = [('leo', 'LEO'), ('geo', 'GEO'), ('interplanetary', 'Interplanetary'),
            ('human', 'Human-Spaceflight')]
    mission_code = models.CharField(max_length=100)
    mission_id = models.AutoField(primary_key=True)
    mission_type = models.CharField(blank=True, max_length=50, choices=TYPE)
    mission_title = models.CharField(max_length=100)
    mission_site = models.CharField(max_length=100)
    mission_date = models.DateField()
    post_thumbnail = models.ImageField(upload_to='', default="")
    mission_YT_link = models.URLField(max_length=200)
    mission_content = models.TextField(max_length=1000)
    mission_lv = models.CharField(max_length=500)
    mission_lv_link = models.URLField(max_length=200)

    mission_payload = models.CharField(max_length=500)
    mission_payload_link = models.URLField(max_length=200)

    mission_link1_Name = models.CharField(max_length=500)
    mission_link1 = models.URLField(max_length=200)

    mission_link2_Name = models.CharField(max_length=500)
    mission_link2 = models.URLField(max_length=200)

    mission_link3_Name = models.CharField(max_length=500)
    mission_link3 = models.URLField(max_length=200)
    mission_thumbs = models.FileField(blank=True)

    def __str__(self):
        return self.mission_title


class MissionImage(models.Model):
    post = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='uploads/')


class Rocket(models.Model):
    rocket_id = models.AutoField(primary_key=True)
    rocket_code = models.CharField(max_length=500)
    rocket_thumb = models.ImageField(upload_to="uploads/", default="")

    rocket_name = models.CharField(max_length=500)
    rocket_subheading = models.CharField(max_length=500)
    rocket_stat1_name = models.CharField(max_length=500)
    rocket_stat1_value = models.IntegerField()
    rocket_stat2_name = models.CharField(max_length=500)
    rocket_stat2_value = models.IntegerField()
    rocket_stat3_name = models.CharField(max_length=500)
    rocket_stat3_value = models.IntegerField()

    # Info Section
    rocket_info = models.TextField(max_length=1000)
    rocket_render = models.TextField(
        max_length=2000)  # update this with HTML field

    # Overview
    rocket_overview_thumb = models.ImageField(upload_to="uploads/", default="")
    rocket_height = models.IntegerField()
    rocket_dia = models.IntegerField()

    rocket_stages = models.IntegerField()
    rocket_lf_mass = models.IntegerField()

    rocket_leo = models.IntegerField()
    rocket_gto = models.IntegerField()

    rocket_stage1_menu_name = models.CharField(max_length=500)
    rocket_stage1_name = models.CharField(max_length=500)
    rocket_stage1_info = models.TextField(max_length=1000)
    rocket_stage1_engine = models.CharField(max_length=500)
    rocket_stage1_fuel = models.CharField(max_length=500)
    rocket_stage1_maxThrust = models.CharField(max_length=500)
    rocket_stage1_thumb = models.ImageField(upload_to="uploads/", default="")

    rocket_stage2_menu_name = models.CharField(max_length=500)
    rocket_stage2_name = models.CharField(max_length=500)
    rocket_stage2_info = models.TextField(max_length=1000)
    rocket_stage2_engine = models.CharField(max_length=500)
    rocket_stage2_fuel = models.CharField(max_length=500)
    rocket_stage2_maxThrust = models.CharField(max_length=500)
    rocket_stage2_thumb = models.ImageField(upload_to="uploads/", default="")

    rocket_stage3_menu_name = models.CharField(max_length=500)
    rocket_stage3_name = models.CharField(max_length=500)
    rocket_stage3_info = models.TextField(max_length=1000)
    rocket_stage3_engine = models.CharField(max_length=500)
    rocket_stage3_fuel = models.CharField(max_length=500)
    rocket_stage3_maxThrust = models.CharField(max_length=500)
    rocket_stage3_thumb = models.ImageField(upload_to="uploads/", default="")

    show = (('block', "block"), ('none', "none"))
    rocket_stage4_show = models.CharField(max_length=10, choices=show)
    rocket_stage4_menu_name = models.CharField(max_length=500)
    rocket_stage4_name = models.CharField(max_length=500)
    rocket_stage4_info = models.TextField(max_length=1000)
    rocket_stage4_engine = models.CharField(max_length=500)
    rocket_stage4_fuel = models.CharField(max_length=500)
    rocket_stage4_maxThrust = models.CharField(max_length=500)
    rocket_stage4_thumb = models.ImageField(upload_to="uploads/", default="")

    rocket_variant_thumb = models.ImageField(upload_to="uploads/", default="")

    # Launch Video
    rocket_launchVideo = models.TextField(max_length=2000)

    def __str__(self):
        return self.rocket_name
