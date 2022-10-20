from django.contrib import admin
from django.urls import path, re_path
from .views import *
from .models import *

urlpatterns = [
    # path('companies/', companies, name="companies"),
    path("companies/", CompanyList.as_view(), name='company-list'),
    # path(r'advocates/^(?P<query>[\w-]+)/$', AdvocateList.as_view(), name="advocates-list"),
    path('advocates/', AdvocateList.as_view(), name="advocates-list"),
    path('companies/<id>', companies_specific, name="companies_individual"),
    path('advocates/<id>', advocates_specific, name="advocates_individual"),
]

# advocates/(?P<query>.+)/$'