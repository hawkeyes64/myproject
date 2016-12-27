from __future__ import unicode_literals
from django.db import models


# Icon Reference
class Reference_LinkIcon(models.Model):
    LinkType = models.CharField(max_length=50)
    IconTagText = models.CharField(max_length=100)

    def __str__(self):
        return self.LinkType


# Create your models here.
class ETab(models.Model):
    tabs_text = models.CharField(max_length=50)
    tabs_anchor = models.CharField(max_length=51)
    tabs_icon = models.CharField(max_length=100, default="icon-file-text")

    def __str__(self):
        return self.tabs_text


# Structured to be 1 class = 1 tab
class AboutMe(models.Model):
    about_me_user = models.CharField(max_length=200)
    about_me_general_role = models.CharField(max_length=200)

    def __str__(self):
        return self.about_me_user


# AboutMe Icon Reference
class AboutMe_Link(models.Model):
    AboutMe_Link_user = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    AboutMe_Link_link = models.CharField(max_length=100)
    AboutMe_Link_icon = models.ForeignKey(Reference_LinkIcon, max_length=30)

    def __str__(self):
        tmp_str = self.AboutMe_Link_user.about_me_user
        tmp_str += " | " + self.AboutMe_Link_icon.LinkType
        return tmp_str


class WorkExperience(models.Model):
    experience_label = models.CharField(max_length=30)
    experience_date_from = models.CharField(max_length=4)
    experience_date_to = models.CharField(max_length=4)
    experience_description = models.CharField(max_length=200)

    def label(self):
        return self.experience_label

    def date_from(self):
        return self.experience_date_from

    def date_to(self):
        return self.experience_date_to

    def description(self):
        return self.experience_description


class CasualExperience(models.Model):
    experience_label = models.CharField(max_length=30)
    experience_date_from = models.CharField(max_length=4)
    experience_date_to = models.CharField(max_length=4)
    experience_description = models.CharField(max_length=200)

    def label(self):
        return self.experience_label

    def date_from(self):
        return self.experience_date_from

    def date_to(self):
        return self.experience_date_to

    def description(self):
        return self.experience_description


class skill_list(models.Model):
    skill_type = models.CharField(max_length=20)
    skill_text = models.CharField(max_length=100)
    skill_bar_color = models.CharField(max_length=30, default="meter asbestos")
    skill_bar_percent = models.FloatField(default=0)

    def type(self):
        return self.skill_type

    def text(self):
        return self.skill_text

    def bar_color(self):
        return self.skill_bar_color

    def bar_percent(self):
        return self.skill_bar_percent
