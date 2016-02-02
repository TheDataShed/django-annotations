import django_rq
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render


def dummy_method(json_string):
    pass


def enqueue(request):
    if request.method == "POST":
        # TODO:
        django_rq.enqueue(dummy_method, request.body)
    else:
        return HttpResponseForbidden()
