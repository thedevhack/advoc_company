from rest_framework import serializers
from .models import *


# class SocialDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Social_Data
#         # fields = "__all__"
#         exclude = ["sdid"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        fields = ["id", "name", "logo", "summary", "advocates"]
        # depth = 1
        # exclude = ["advocates"]

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    # links = SocialDataSerializer()
    class Meta:
        model = Advocate
        fields = ["id","profile_pic", "username", "name" ,  "bio", "twitter" , "company"]

class EachAdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    # links = SocialDataSerializer()

    class Meta:
        model = Advocate
        fields = ["id","profile_pic", "username", "name" ,  "bio", "twitter" , "company"]
        # depth = 2

class EachCompanySerializer(serializers.ModelSerializer):
    advocates = AdvocateSerializer(many=True)
    class Meta:
        model = Company
        fields = ["id", "name", "logo", "summary", "advocates"]
        # depth = 1