from django.contrib import admin
from django.urls import path, re_path
from .views import *
from .models import *

urlpatterns = [
    path('', home, name="home"),
    path("companies/", CompanyList.as_view(), name='company-list'),
    # path(r'advocates/^(?P<query>[\w-]+)/$', AdvocateList.as_view(), name="advocates-list"),
    path('advocates/', AdvocateList.as_view(), name="advocates-list"),
    path('advocates/<int:id>', advocates_specific, name="advocates_individual"),
    path('advocates/<str:username>', advocates_list_specific, name="advocates-list-queryed"),
    path('companies/<int:id>', companies_specific, name="companies_individual"),
    
]