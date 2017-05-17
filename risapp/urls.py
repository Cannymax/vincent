from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^search/$', views.search, name='search'),
    url(r'^clarifai/search/$', views.search_by_clarifai, name='search_by_clarifai'),
    url(r'^clarifai/concepts/$', views.search_by_predicted_concepts, name='search_by_concepts'),
    url(r'^clarifai/predict/$', views.predict_by_clarifai, name='predict_by_clarifai'),
]
