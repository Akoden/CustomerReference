
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from csr.utils import render_ext

# @login_required
def index(req):
    return render_to_response('index.html')


@login_required
@render_ext('secure')
def secure(req):
    return ('render', 'secure.html')

@render_ext('home')
def home(req):
    return ('render', 'home.html')

@render_ext('what_s_hot')
def what_s_hot(req):
    return ('render', 'what_s_hot.html')

@render_ext('customers')
def customers(req):
    return ('render', 'customers.html')

@render_ext('add_customer')
def add_customer(req):
    return ('render', 'add_customer.html')

@render_ext('add_reference')
def add_reference(req):
    return ('render', 'add_reference.html')

@render_ext('help')
def help(req):
    return ('render', 'help.html', {'view_id':'home'})
    
