from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request == 'POST':
        print (request.POST[''])

    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')