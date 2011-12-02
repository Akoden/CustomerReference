#
from django import forms
from src.csr.models import Account
from django.contrib.auth.models import User

from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
import django.contrib.auth as auth

from django.http import HttpResponseRedirect, HttpResponse
import simplejson
from csr.utils import render_ext


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

def create_account(): pass


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
                # create account if not exists
                try:
                    accnt = Account.objects.get(username=username)
                except Account.DoesNotExist:
                    Account(username=username, firstname=username).save()
                # redirect to 'next' view
	        next_view = request.GET.get('next')
		if next_view:
		    return ('redirect', next_view)
		return ('success', {'username': username})
            else:
                # Return a 'disabled account' error message
		return ('disabled', {'username': username})   
    # return render(request, 'accounts/login.html', {'form': form})
    return ('error', { 'form': form })


@csrf_protect
@render_ext('',
    { 'success':  {'location': 'accounts/account.html'} })
def account(request):
    return ('success', {'account': Account.objects.get(username=request.user)})


@render_ext('')
def logout(request):
   auth.logout(request)
   return ('redirect', '/')


def init_users():
    if User.objects.all().count() <= 1:
        User.objects.create_user('jbrown', 'jeremy@akoden.com', 'jbr0wn')
        User.objects.create_user('rtheo',  'theo@akoden.com', 'rthe0')
        User.objects.create_user('azopat', 'azopat@akoden.com', 'az0pat')

init_users()
        
