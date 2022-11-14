import os
from collections import Counter
from pickle import GET

from django.db.models import Q
from django.shortcuts import get_object_or_404
from konlpy.tag import Okt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()
#여기까지 입력 안해주면 오류뜸

from numpy import dot
from numpy.linalg import norm
import numpy as np

from pybo.models import Maincont

if __name__ == '__main__':
    maincont=Maincont.objects.values_list('word')    #단어만 출력  > '단어' 칼럼(열)
    # print(list(maincont))  #쿼리셋 / list로 maincont를 감싸줘야지 제대로 뜸 > 아니면 오버라이딩 됨

    okt=Okt()
    b=[]
    num_list = []
    word_list=[]
    sent=''+str(list(maincont))    #list로 maincont를 감싸줘야지 제대로 뜸 > 아니면 오버라이딩 됨
    b=okt.nouns(sent)

    # print(b)   #전체 단어(명사) 리스트로 출력

    count=Counter(b)
    noun_list = count.most_common((7))

    # print(noun_list)    #[(명사,빈도),(명사,빈도),(명사,빈도)]

    for v in noun_list:
        num_list.append(v[1])

    for i in noun_list:
        word_list.append(i[0])

    # print(num_list)   #빈도수 출력
    # print(word_list)  #전체단어 출력 / 빈도수 높은 단어 출력
    # print('\n')

    # 단어 중에서 '아이디' 에 따라 한번더 필터링함 'admin' 대신 request.user씀
    maincont_my = maincont.filter(author__username__icontains ='admin' )

    # print(list(maincont_my))   #각자 유저들의 단어들만 출력


    maincont_sentence= Maincont.objects.values_list('sentence')  # 문장만 출력  > '문장' 칼럼(열) : 전체 사용자
    '''
    print(list(maincont_sentence))#전체 저장된 문장들 리스트로 오버라이딩 없이 출력
    lists=list(maincont_sentence)
    sen_all=[]

    for sen in lists:
        sen_all.append(sen[0])
    print(sen_all)  #튜플 > 리스트로
    str_all="".join(sen_all)
    print(str_all)  #리스트 > 문자열
    '''

    ex_sentence = " 33 "

    maincont_my_sentence = maincont_sentence.filter(author__username__icontains = "julie" ) #'admin'유저의 문장들

    print(list(maincont_my_sentence)) #admin유저의 저장된 문장데이터 전체 출력 > 리스트 안에 튜플 있음

    lists_my=list(maincont_my_sentence)
    sen_my=[]

    for sen in lists_my:
        sen_my.append(sen[0])
    # print(sen_my)  #튜플 > 리스트
    str_my="".join(sen_my)
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


    print( "예시 문장  <-> 나의 전체 문장들 : 관련 유사도 " , round(cs1*100,1) )  # 퍼센티지로 나타냄 , 소수점 첫째자리 반올림



