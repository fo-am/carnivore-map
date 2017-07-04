from django.shortcuts import get_object_or_404, render, render_to_response
from map.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django import forms
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import Context, loader, RequestContext
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _


# Create your views here.
class IncidentsView(generic.ListView):
    queryset = Incident.objects.all()
    template_name = 'map/index.html'
    def get_context_data(self, **kwargs):
        context = super(IncidentsView,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class IncidentView(generic.DetailView):
    model = Incident
    template_name = 'map/incident.html'
    def get_context_data(self, **kwargs):
        context = super(IncidentView,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class IncidentForm(CreateView):
    model = Incident
    fields = "__all__"
    success_url="/"

# Create your views here.
class UserView(generic.ListView):
    template_name = 'map/user.html'
    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(UserView,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


## user stuff ######################################################

class UserForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'),widget=forms.PasswordInput())
    repeat_password = forms.CharField(label=_('Repeat password'),widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'repeat_password')

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if not repeat_password:
            raise forms.ValidationError("You must confirm your password")
        if password != repeat_password:
            raise forms.ValidationError("Your passwords do not match")
        return repeat_password



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age_range','gender')

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'])
            login(request, new_user)
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    if registered:
        return HttpResponseRedirect('/')
    else:
        return render_to_response(
            'map/register.html',
            {'user_form': user_form,
             'profile_form': profile_form,
             'registered': registered },
            context)

def logmein(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse(_("Your account is disabled."))
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse(_("Invalid login details supplied."))

    else:
        return render_to_response('map/login.html', {}, context)

def logmeout(request):
    logout(request)
    return HttpResponseRedirect('/')
