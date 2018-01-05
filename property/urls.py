from django.conf.urls import url
from django.views.generic import TemplateView
from .views import compare_property, add_property, PropertySerializerView, delete_property
from .models import Property

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="property/home.html"), name="all_properties"),
    url(r'^add/', add_property, name="add_property"),
    url(r'^compare/', compare_property, name="compare_property"),
    url(r'^rest-api/$', PropertySerializerView.as_view(), name="property_serializer"),
    url(r'^rest-api/delete/(?P<pk>[0-9]+)/$', delete_property, name="delete_property")
]
