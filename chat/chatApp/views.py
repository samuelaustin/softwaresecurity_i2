# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

@login_required(redirect_field_name='chatApp/index.html')
def index(request):
	if request.method == 'POST':
		input = request.POST.get('message')
		m = Message(text=input,date=timezone.now(),uid_id=1)
		m.save();

	message_list = Message.objects.order_by('-date')
	context = {'message_list': message_list}
	return render(request, 'chatApp/index.html', context)

def Login(request):
	next = request.GET.get('next', '/chatApp/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				print("Het is gelukt !!!!")
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Inactive user.")
		else:
			print("Het is NIET gelukt !!!!")
			return HttpResponseRedirect('/chatApp/login/')

	return render(request, "chatApp/login.html", {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect('/chatApp/login/')

def Register(request):
	if request.method == 'POST':
		print("Het is een POST ding!!!!")
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			new_user = form.save()
			print("Form saved")
			return HttpResponseRedirect("/chatApp/")
		else:
			print("Form not valid")
			print(form.errors)
	else:
		print("Het is NIET een POST ding!!!!")
		form = UserCreationForm()
	return render(request, "chatApp/register.html", {
		'form': form,
	})