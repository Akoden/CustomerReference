
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Customer, Reference
from django.forms import ModelForm, Textarea

from csr.utils import render_ext

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        widgets = {
            'story': Textarea(attrs={'cols': 80, 'rows': 20}),
            }


# @login_required
@render_ext('home')
def index(req):
    return ('render', 'index.html')


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

##
##
@render_ext('customers', { 'success':  {'location': 'customers.html'}})
def customers(req):
    return ('success', {'customers': Customer.objects.filter()})


@login_required
@render_ext('add_customer',
    { 'success':  {'location': 'add_customer.html'},
      'error':    {'location': 'add_customer.html'} })
def add_customer(req):
    form = CustomerForm(req.POST) if (req.method == 'POST') else CustomerForm()
    if req.method == 'POST':
        if form.is_valid():
            # save form
            form.save()
            return ('redirect', '/customers/')
        else:
            return ('error', {'form': form})
    return ('success', { 'form': form })

##
##
@render_ext('references', { 'success':  {'location': 'references.html'}})
def references(req):
    return ('success', {'references': Reference.objects.filter()})

@login_required
@render_ext('add_reference',
    { 'success':  {'location': 'add_reference.html'},
      'error':    {'location': 'add_reference.html'} })
def add_reference(req):
    form = ReferenceForm(req.POST) if (req.method == 'POST') else ReferenceForm()
    if req.method == 'POST':
        if form.is_valid():
            # save form
            form.save()
            return ('redirect', '/references/')
        else:
            return ('error', {'form': form})
    return ('success', {'form': form})


@login_required
@render_ext('references', { 'success':  {'location': 'reference.html'}})
def reference(req, ref_id):
    try:
        return ('success', {'reference': Reference.objects.get(id=ref_id)})
    except:
        return ('not-found', '')

@render_ext('help')
def help(req):
    return ('render', 'help.html', {'view_id':'home'})
    
