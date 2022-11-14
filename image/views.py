
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from tesseract.tesseract import Convert


def image_view(request):
    return render(request, 'image/image.html')



def image_convert(request):
    t = Convert()
    context = t.tesseract()  # 딕셔너리 반환

    return JsonResponse(context)
