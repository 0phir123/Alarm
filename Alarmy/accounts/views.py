from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):

    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
        auth.login(request, user)
        messages.success(request, 'U are now logged in')
        return redirect('setup')

      else:
        messages.error(request, 'Wrong user\pass')
        return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
     
      auth.logout(request)
      messages.success(request, 'u are now logged out , Thanks You for visiting my website')
      return redirect('index')