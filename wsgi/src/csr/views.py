
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

# @login_required
def index(req):
    return render_to_response('index.html')


@login_required
def secure(req):
    return render_to_response('secure.html')

def home(req):
    return render_to_response('home.html')

def what_s_hot(req):
    return render_to_response('what_s_hot.html')

def customers(req):
    return render_to_response('customers.html')

def add_customer(req):
    return render_to_response('add_customer.html')

def add_reference(req):
    return render_to_response('add_reference.html')

def help(req):
    return render_to_response('help.html')
    
