from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse('This Is Home Page')

    
def about(request):
    return HttpResponse('This Is about Page')

def services(request):
    return HttpResponse('This Is services Page')

def contact(request):
    return HttpResponse('This Is contact Page')

