from django.shortcuts import render

# Create your views here.
def home_site(request):
    return render(request, 'base.html' )
def home_order(request):
    return render(request, 'order/index.html' )