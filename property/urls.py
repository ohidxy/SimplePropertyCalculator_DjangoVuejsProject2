from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CompareProperty, Property

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="property/home.html")),
    url(r'^add/', Property.as_view(), name="add_property"),
    url(r'^compare/', CompareProperty.as_view(), name="compare_property"),
]
