from django.shortcuts import render, HttpResponse, redirect, render_to_response
import json
from django.utils.safestring import mark_safe


# def login(request):
#     return render(request,'login.html')
def home(request):
    # return HttpResponse('home')  loads home html page

    return render(request, 'home.html')


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response(request, ctx)


def room(request, room_name):  # stores room name in json format and loads room html
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
