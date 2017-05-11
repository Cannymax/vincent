from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'risapp.views.home', name='home'),
    url(r'^about/$', 'risapp.views.about', name='about'),
    url(r'^pricing/$', 'risapp.views.pricing', name='pricing'),
    url(r'^contact/$', 'risapp.views.contact', name='contact'),

    url(r'^search/$', 'risapp.views.search', name='search'),
    url(r'^search-clarifai/$', 'risapp.views.search_by_clarifai', name='search_by_clarifai'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
