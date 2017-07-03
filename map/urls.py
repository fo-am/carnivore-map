from django.conf.urls import patterns, url
from django.conf.urls import include

from map import views

urlpatterns = patterns('',
    url(r'^$', views.IncidentsView.as_view(), name='index'),
    url(r'^incident/(?P<pk>\d+)/$', views.IncidentView.as_view(), name='incident'),                     
    url(r'^add/$', views.IncidentForm.as_view(), name='add'),                     
)

