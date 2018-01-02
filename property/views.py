from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class Property(TemplateView):
    def get(self, request):
        return render(request, 'property/add_property.html', {})

class CompareProperty(TemplateView):
    def get(self, request):
        return render(request, 'property/compare_property.html', {})



