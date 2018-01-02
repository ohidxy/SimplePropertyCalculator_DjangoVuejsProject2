from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name='property/home.html'
    def get_context_data(self, **kwargs):
        context = dict(Property.objects.all())
        return context

class PropertyView(TemplateView):
    def get(self, request):
        return render(request, 'property/add_property.html', {})

class CompareProperty(TemplateView):
    def get(self, request):
        return render(request, 'property/compare_property.html', {})



