
from django.shortcuts import render

def index(request):
    # depricated
    return render(request, 'home/index.html')
