from django.shortcuts import render
from .models import Property


from .serializers import PropertySerializer


from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView


def all_property(request):
    return render(request, 'property/home.html')

def add_property(request):
    return render(request, 'property/add_property.html')

def compare_property(request):
    return render(request, 'property/compare_property.html')


class PropertySerializerView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


