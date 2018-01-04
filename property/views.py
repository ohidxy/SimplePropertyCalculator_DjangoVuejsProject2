from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Property
from .forms import AddProperty, AddPropertyType
from rest_framework.views import APIView
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_bulk import ListCreateBulkUpdateAPIView


class PropertyListView(ListView):
    model = Property
    template_name='property/home.html'

    def post(self, request):
        return HttpResponse('Works!')

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context['property'] = Property.objects.all()
        return context

class AddPropertyView(TemplateView):
    def get(self, request):
        property_form = AddProperty()
        properttype_form = AddPropertyType()
        context = {
          'property_form': property_form, 
          'properttype_form': properttype_form
        }
        return render(request, 'property/add_property.html', context)
    

class CompareProperty(TemplateView):
    def get(self, request):
        return render(request, 'property/compare_property.html', {})


class PropertySerializerView(APIView):
    def get(self, request):
        all_properties = Property.objects.all()
        serializer = PropertySerializer(all_properties, many=True)
        return Response(serializer.data)

    def put(self, request):
        instances = []
        serializer = PropertySerializer(data=request.data, instance = instances, many=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertySerializerView2(ListCreateBulkUpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


