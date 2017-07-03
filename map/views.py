from django.shortcuts import render
from map.models import *
from django.views import generic
from django import forms
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class IncidentsView(generic.ListView):
    queryset = Incident.objects.all()
    template_name = 'map/index.html'

class IncidentView(generic.DetailView):
    model = Incident
    template_name = 'map/incident.html'

class IncidentForm(CreateView):
    model = Incident
    fields = "__all__"
    success_url="/"
