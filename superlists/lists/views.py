from django.shortcuts import render
from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse(b'<html><title>To-Do lists</title></html>')

