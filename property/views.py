from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Property
from .forms import AddProperty


class PropertyListView(ListView):
    model = Property
    template_name='property/home.html'

    def post(self, request):
        return HttpResponse('Works!')

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context['property'] = Property.objects.all()
        return context

class PropertyView(TemplateView):
    def get(self, request):
        form = AddProperty()
        return render(request, 'property/add_property.html', {'form': form})
    

class CompareProperty(TemplateView):
    def get(self, request):
        return render(request, 'property/compare_property.html', {})



