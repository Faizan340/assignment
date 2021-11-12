from django.shortcuts import render,HttpResponse

# Create your views here.
def product(request):
    return HttpResponse('hello world')