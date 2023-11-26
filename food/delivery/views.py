from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def index(request):
    request.session.set_expiry(0)
    print(request.session['order'])
    context = {
        'active_link': 'index',
    }
    return render(request, 'index.html')

def burger(request):
    request.session.set_expiry(0)
    burger_data = Burgers.objects.all()
    context = {
        'menu': burger_data,
        'active_link': 'burger', 
    }
    return render(request, 'burger.html', context)

def AddOn(request):
    request.session.set_expiry(0)
    AddOn_data = AddOns.objects.all()
    context = {
        'menu': AddOn_data,
        'active_link': 'AddOn',
    }
    return render(request, 'AddOn.html', context)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        print(request.session['note'])
        request.session['order'] = request.POST.get('orders')
        print(request.session['order'])
    context = {
        'active_link': 'order',
    }
    return render(request, 'order.html', context)

def success(request):
    order = request.session['order']
    context = {
        'order': order,
    }
    return render(request, 'success.html', context)