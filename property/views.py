from django.shortcuts import render
from .models import Property
from .serializers import PropertySerializer
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def all_property(request):
    return render(request, 'property/home.html')

def add_property(request):
    return render(request, 'property/add_property.html')

def compare_property(request):
    return render(request, 'property/compare_property.html')


class PropertySerializerView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

@api_view(['DELETE'])
def delete_property(request, pk):
    if request.method == 'DELETE':
        try:
            prop = Property.objects.get(pk=pk)
        except prop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


