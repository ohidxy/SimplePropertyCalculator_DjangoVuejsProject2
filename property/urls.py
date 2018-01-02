from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompareProperty, PropertyView, PropertyListView
from .models import Property

urlpatterns = [
    url(r'^$', PropertyListView.as_view(), name="all_properties"),
    url(r'^add/', PropertyView.as_view(), name="add_property"),
    url(r'^compare/', CompareProperty.as_view(), name="compare_property"),
]
