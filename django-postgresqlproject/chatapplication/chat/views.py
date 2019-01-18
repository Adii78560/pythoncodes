from django.shortcuts import render, HttpResponse, redirect
import json
from django.utils.safestring import mark_safe


def home(request):
    # return HttpResponse('home')  loads home html page

    return render(request, 'registration/home.html')


def room(request, room_name):   # stores room name in json format and loads room html
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

