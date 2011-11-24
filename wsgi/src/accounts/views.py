#
from django import forms

from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
import django.contrib.auth as auth

from django.http import HttpResponseRedirect, HttpResponse
import simplejson


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

@csrf_protect
def login(request):
    form = LoginForm(request.POST) if (request.method == 'POST') else LoginForm()
    is_ajax = request.GET.get('ajax') 
    if request.method == 'POST' and form.is_valid():
        username, password = form.cleaned_data['username'], form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                # Redirect to a success page.
	        next_view = request.GET.get('next')
		if is_ajax:
		    return HttpResponse(simplejson.dumps({'result' : 'success', 'username':username}), mimetype='application/json')
	        return HttpResponseRedirect(next_view if next_view else '/welcome/')
            else:
                # Return a 'disabled account' error message
		if is_ajax:
		    return HttpResponse(simplejson.dumps({'result' : 'error', 'status': 'disabled-account'}), mimetype='application/json')
	        return HttpResponseRedirect('/accounts/disabled/')     
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
   auth.logout(request)
   return HttpResponseRedirect('/accounts/login/')
