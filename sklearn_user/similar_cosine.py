import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.shortcuts import get_object_or_404
from pybo.models import Maincont

import numpy as np
from numpy import dot
from numpy.linalg import norm
from konlpy.tag import Okt



class Similar_cos:
    def __init__(self,sentences, lists):
        self.sentences=sentences #maincont.sentence 넘겨받음
        self.lists = lists      #리스트 넘겨받음

    def my_similar(self):
        okt=Okt()

        ex_sentence = self.sentences  #각각의 문장 들어옴

        # print(list(maincont_my_sentence)) #admin유저의 저장된 문장데이터 전체 출력 > 리스트 안에 튜플 있음
        lists_my = list(self.lists)
        sen_my = []

        for sen in lists_my:
            sen_my.append(sen[0])
        # print(sen_my)  #튜플 > 리스트
        str_my = "".join(sen_my)

        # print(str_my)  #리스트 > 문자열

        # 코사인 유사도를 구하는 함수
        def cos_sim(a, b):
            return dot(a, b) / (norm(a) * norm(b))

        # 기준이 되는 키워드와 벡터 키워드 리스트를 받아서 키워드별 빈도를 구하는 함수
        def make_matrix(feats, list_data):
            freq_list = []
            for feat in feats:
                freq = 0
                for word in list_data:
                    if feat == word:
                        freq += 1
                freq_list.append(freq)
            return freq_list

        text1 = ex_sentence
        text2 = str_my

        v1 = okt.nouns(text1)
        v2 = okt.nouns(text2)

        # 단어들을 중복제거를 위해, set에 데이터를 쌓는다
        v4 = v1 + v2
        feats = set(v4)

        v1_arr = np.array(make_matrix(feats, v1))
        v2_arr = np.array(make_matrix(feats, v2))

        cs1 = cos_sim(v1_arr, v2_arr)
        return round(cs1*100,1) # 퍼센티지로 나타냄 , 소수점 첫째자리 반올림 / my_similar 함수 최종 리턴


