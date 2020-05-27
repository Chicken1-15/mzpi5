from django.shortcuts import render
from .forms import *
import requests

def user_data():
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/user'
    result = requests.get(url, auth=('kiosk03', 'kiosk03'))
    return result.json()

def area_data():
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/area'
    result = requests.get(url, auth=('kiosk03', 'kiosk03'))
    return result.json()

def tasks_data():
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/robots/tasks/all'
    result = requests.get(url, auth=('kiosk03', 'kiosk03'))
    return result.json()

def log_in(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        pass
    context = {
        'form': form
    }
    return render(request, 'select.html', context)

def robot_poke(request):
    pass

def robot_dismiss(request):
    pass

def data(request):
    return render(request, 'data.html', {'list': tasks_data()})

