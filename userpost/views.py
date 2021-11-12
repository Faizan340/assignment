from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def userpost(request):
    #user = User.objects.create_user('faizan123', 'abcd@.com', '1234')
    #user.first_name= 'faizan'
    #user.last_name='rashid'
    #user.save()
    return HttpResponse('hello earth')