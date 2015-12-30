# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Message
from django import forms
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

@login_required(redirect_field_name='chatApp/index.html')
def index(request):
    if request.method == 'POST':
        input = request.POST.get('message')
        m = Message(text=input,date=timezone.now(),uid_id=1)
        m.save();

    message_list = Message.objects.order_by('-date')
    context = {'message_list': message_list}
    return render(request, 'chatApp/index.html', context)

def my_login(request):
	return HttpResponse("Hello, world. You're at the Login Page.")

def login_user(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
	    username = request.POST.get('username')
	    password = request.POST.get('password')

	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            state = "You're successfully logged in!"
	        else:
	            state = "Your account is not active, please contact the site admin."
	    else:
	        state = "Your username and/or password were incorrect."

	return render_to_response('auth.html',{'state':state, 'username': username})
