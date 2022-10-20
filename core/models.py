from django.db import models
import uuid


class Social_Data(models.Model):
    sdid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    youtube = models.URLField(max_length = 300)
    twitter = models.URLField(max_length = 300)
    github = models.URLField(max_length = 300)

class Company(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.URLField(max_length = 300)
    summary = models.CharField(max_length = 400, default="")
    advocates = models.ManyToManyField('Advocate', related_name="advocates", default="", blank=True)
    href = models.CharField(max_length = 100,default = "", blank = True, null=True)


class Advocate(models.Model):
    name = models.CharField(max_length = 200)
    profile_pic = models.URLField(max_length = 300)
    short_bio = models.CharField(max_length = 300, blank=True)
    long_bio = models.CharField(max_length = 400, null=True, blank=True)
    advocate_years_exp = models.IntegerField(default = 0)
    company = models.ForeignKey(Company, null = True, on_delete=models.SET_NULL)
    links = models.OneToOneField(Social_Data, null = True, on_delete=models.SET_NULL)
