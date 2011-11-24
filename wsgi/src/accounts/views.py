#
from django import forms

from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
import django.contrib.auth as auth

from django.http import HttpResponseRedirect, HttpResponse
import simplejson
from csr.utils import render_ext


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

@csrf_protect
@render_ext('',
    { 'success':  {'location': '/welcome/successful-login'},
      'disabled': {'location': 'accounts/login.html'},
      'error':    {'location': 'accounts/login.html'} })
def login(request):
    form = LoginForm(request.POST) if (request.method == 'POST') else LoginForm()
    if request.method == 'POST' and form.is_valid():
        username, password = form.cleaned_data['username'], form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user) 
	        next_view = request.GET.get('next')
		if next_view:
		    return ('redirect', next_view)
		return ('success', {'username': username})
            else:
                # Return a 'disabled account' error message
		return ('disabled', {'username': username})   
    # return render(request, 'accounts/login.html', {'form': form})
    return ('error', { 'form': form })


@render_ext('')
def logout(request):
   auth.logout(request)
   return ('redirect', '/accounts/login/')
