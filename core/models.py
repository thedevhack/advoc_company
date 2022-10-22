from django.db import models
import uuid


# class Social_Data(models.Model):
#     sdid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     youtube = models.URLField(max_length = 300, blank = True, null=True)
#     twitter = models.URLField(max_length = 300, blank = True, null=True)
#     github = models.URLField(max_length = 300, blank = True, null=True)

class Company(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.URLField(max_length = 300)
    summary = models.CharField(max_length = 400, default="")
    advocates = models.ManyToManyField('Advocate', related_name="advocates", default="", blank=True)
    href = models.CharField(max_length = 100,default = "", blank = True, null=True)


class Advocate(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200, blank = True, null = True)
    profile_pic = models.URLField(max_length = 300)
    bio = models.CharField(max_length = 500, blank=True)
    twitter = models.URLField(max_length = 300, blank = True, null=True)
    # long_bio = models.CharField(max_length = 400, null=True, blank=True)
    # advocate_years_exp = models.IntegerField(default = 0)
    company = models.ForeignKey(Company, null = True, on_delete=models.SET_NULL)
    # links = models.OneToOneField(Social_Data, null = True,blank=True, on_delete=models.SET_NULL)