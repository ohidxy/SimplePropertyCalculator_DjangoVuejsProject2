from django.shortcuts import render, redirect
from .models import Property
from .serializers import PropertySerializer
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import AddProperty

def add_property(request):
    if request.method == "POST":
        form = AddProperty(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = AddProperty()
        return render(request, 'property/add_property.html', {'property_form': form})

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
    


