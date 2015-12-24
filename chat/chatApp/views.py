# Create your views here.
from django.shortcuts import render
from .models import Message
from django.views import generic


def index(request):
    message_list = Message.objects.order_by('-date')

    context = {'message_list': message_list}

    return render(request, 'chatApp/index.html', context)
