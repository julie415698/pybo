from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return render(request, 'pybo/home.html')   #html 반환