from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from .paginations import HackPagination


# @api_view(['GET'])
# def companies(request):
#     data = Company.objects.all()
#     serializered_data = CompanySerializer(data, many=True)
#     return Response({'status': 200, 'payload':serializered_data.data})

# @api_view(['GET'])
# def advocates(request):
#     data = Advocate.objects.all()
#     serializered_data = AdvocateSerializer(data, many=True)
#     return Response({'status': 200, 'payload':serializered_data.data})

@api_view(['GET'])
def companies_specific(request, id):
    data = Company.objects.get(id=id)
    serializered_data = EachCompanySerializer(data)
    return Response({'status': 200, 'payload':serializered_data.data})

@api_view(['GET'])
def advocates_specific(request, id):
    data = Advocate.objects.get(id=id)
    serializered_data = EachAdvocateSerializer(data)
    return Response({'status': 200, 'payload':serializered_data.data})


class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer
    pagination_class = HackPagination

    def get_queryset(self):
        queryset = Company.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class AdvocateList(generics.ListAPIView):
    serializer_class = AdvocateSerializer
    pagination_class = HackPagination

    def get_queryset(self):
        queryset = Advocate.objects.all()

        query = self.request.query_params.get('query')
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset