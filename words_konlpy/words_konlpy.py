import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()


from konlpy.tag import Okt
from collections import Counter

from pybo.models import Maincont



class Chart_konlpy:
    def __init__(self,lists):
        self.lists = lists      #리스트 넘겨받음

    #빈도수에 대한 단어 리스트 return
    def  word_show(self):
        okt=Okt()
        a=[]
        word_list = []
        sent = '' + str(self.lists)     #리스트를 문자열로 바꿈
        a=okt.nouns(sent)
        count=Counter(a)
        noun_list=count.most_common((7))
        for v in noun_list:
            word_list.append(v[0])
        return word_list

    #단어에 대한 빈도수 리스트 return
    def num_show(self):
       okt = Okt()
       a = []
       num_list = []
       sent = '' + str(self.lists)
       a = okt.nouns(sent)
       count = Counter(a)
       noun_list = count.most_common((7))
       for v in noun_list:
           num_list.append(v[1])
       return num_list



#print(Maincont.objects.values_list('word'))  #쿼리셋

#maincont=Maincont.objects.values_list('word')  #쿼리셋 > 리스트로 바꿔서 넣어줌 : 오버라이딩 방지

#chart=Chart_konlpy(list(maincont))  #객체에 문자열로 넘겨줌
#print(chart.word_show())
#print(chart.num_show())

