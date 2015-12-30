# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Message
from django import forms
from django.views import generic

def index(request):
    if request.method == 'POST':
        input = request.POST.get('message')
        m = Message(text=input,date=timezone.now(),uid_id=1)
        m.save();

    message_list = Message.objects.order_by('-date')
    context = {'message_list': message_list}
    return render(request, 'chatApp/index.html', context)