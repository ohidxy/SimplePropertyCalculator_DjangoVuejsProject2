from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompareProperty, AddPropertyView, PropertyListView, PropertySerializerView2
from .models import Property

urlpatterns = [
    url(r'^$', PropertyListView.as_view(), name="all_properties"),
    url(r'^add/', AddPropertyView.as_view(), name="add_property"),
    url(r'^compare/', CompareProperty.as_view(), name="compare_property"),
    url(r'^rest-api/', PropertySerializerView2.as_view(), name="property_serializer")
]
