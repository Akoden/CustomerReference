#

from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
    return render(request, 'accounts/login.html', {})


