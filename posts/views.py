from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from datetime import datetime


# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first view!')


def youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')


def google_view(request):
    if request.method == 'GET':
        return redirect('https://www.google.com')


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project')


def now_date(request):
    if request.method == 'GET':
        current_time = datetime.datetime.now()
        return HttpResponse(current_time)


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user')
