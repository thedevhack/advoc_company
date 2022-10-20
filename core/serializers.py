from rest_framework import serializers
from .models import *


class SocialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_Data
        # fields = "__all__"
        exclude = ["sdid"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        # depth = 1
        # exclude = ["advocates"]

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    links = SocialDataSerializer()
    class Meta:
        model = Advocate
        fields = ["id", "name", "profile_pic", "short_bio", "long_bio", "advocate_years_exp", "company", "links"]

class EachAdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    links = SocialDataSerializer()

    class Meta:
        model = Advocate
        fields = ["id", "name", "profile_pic", "short_bio", "long_bio", "advocate_years_exp", "company", "links"]

class EachCompanySerializer(serializers.ModelSerializer):
    advocates = AdvocateSerializer(many=True)
    class Meta:
        model = Company
        fields = ["id", "name", "logo", "summary", "advocates"]
        # depth = 1