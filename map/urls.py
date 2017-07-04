from django.conf.urls import patterns, url
from django.conf.urls import include

from map import views

urlpatterns = patterns('',
    url(r'^$', views.IncidentsView.as_view(), name='index'),
    url(r'^incident/(?P<pk>\d+)/$', views.IncidentView.as_view(), name='incident'),                     
    url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='user'),                     
    url(r'^add/$', views.IncidentForm.as_view(), name='add'),                     
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.logmein, name='login'),
    url(r'^logout/$', views.logmeout, name='logout'),
)

