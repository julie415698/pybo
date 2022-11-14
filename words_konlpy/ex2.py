from django.db.models import Q
from django.shortcuts import get_object_or_404
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()
from pybo.models import Similar, Maincont

similar2 = Similar.objects.values_list('maincont').distinct()
similar3 = similar2.filter(author__username__icontains = 'admin').order_by('-similar')   #'maincont:게시글'& admin사용자 & 유사도 높은순으로 출력

maincont_list = Maincont.objects.filter(author__username__icontains='admin')
print("admin이 쓴글 쿼리셋 ",maincont_list)
maincont_list1 = Maincont.objects.order_by('-create_date')
print('기존의 것 ',maincont_list1)

print(similar2)
print(similar3)

lists=list(similar3)
#print(list) # 2번쨰가 게시글번호
similar_list=[]

for v in lists:
    similar_list.append(v[0])

print(similar_list)  #similar높은 순서대로 게시글 번호
a=Maincont.objects.filter(id=0)

for i in similar_list:
    print(i)
    print(Maincont.objects.filter(id=i))
    a =a | Maincont.objects.filter(id=i)
    a.update()

print(a)
maincont_list = Maincont.objects.order_by('-create_date')
print(maincont_list)


#print(   maincont_list.union(  Maincont.objects.filter(id=63) | Maincont.objects.filter(id=96)  )  )



'''
similar = Similar.objects.values_list('similar') #similar 쿼리셋으로 가져오기
similar_maincont = Similar.objects.values_list('maincont') #게시글 번호 쿼리셋으로 가져오기

my_similar = similar.filter(author__username__icontains = 'admin')  #현재 사용자의 데이터로 정제,중복제거 > request.user
my_similar_maincont = similar_maincont.filter(author__username__icontains = 'admin')
my_filter = Similar.objects.filter(Q('similar') & Q('maincont'))
#print(my_filter)

similar_num=[]

for v in my_similar:
    similar_num.append(v[0])

print(Similar.objects.all())
print(my_similar_maincont)
print(my_similar)  #쿼리셋 형태로 similar 출력
print(similar_num)  #리스트 형태로 [17, 5,13,0.....] 중복 제거하고 나옴

#Maincont 쿼리셋 형태로 바꿔줘야함


'''