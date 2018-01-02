from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Property
from .forms import AddProperty, AddPropertyType


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



