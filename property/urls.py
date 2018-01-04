from django.conf.urls import url
from django.views.generic import TemplateView
from .views import compare_property, add_property, all_property, PropertySerializerView
from .models import Property

urlpatterns = [
    url(r'^$', all_property, name="all_properties"),
    url(r'^add/', add_property, name="add_property"),
    url(r'^compare/', compare_property, name="compare_property"),
    url(r'^rest-api/', PropertySerializerView.as_view(), name="property_serializer")
]
