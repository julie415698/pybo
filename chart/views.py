import os

from django.db.models import Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()


from django.shortcuts import render
from pybo.models import Maincont
from words_konlpy.words_konlpy import Chart_konlpy



def chart_view(request):
    maincont = Maincont.objects.values_list('word')  #전체 단어에 대한 쿼리셋 데이터
    chart = Chart_konlpy(list(maincont))  #리스트형태로 바꿔서 넣어줌
    context = {'chart':chart}
    return render(request, 'chart/chart.html',context)  # html 반환


def mychart_view(request):
    maincont = Maincont.objects.values_list('word')   #전체 단어에 대한 쿼리셋 데이터
    my_maincont = maincont.filter(author__username__icontains = request.user)  #현재 사용자의 데이터로 정제
    my_chart = Chart_konlpy(list(my_maincont))  # 리스트형태로 바꿔서 넣어줌
    context = {'my_chart': my_chart}
    return render(request, 'chart/my_chart.html', context)
