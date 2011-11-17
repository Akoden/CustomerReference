from django.shortcuts import render_to_response

def login(request):
    return render_to_response('accounts/login.html')


