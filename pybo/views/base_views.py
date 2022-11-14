#기본 ( index창 , detail창)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q, Count   #OR 조건으로 데이터를 검색하는 장고의 함수
from django.views.decorators.csrf import csrf_exempt

from sklearn_user.similar_cosine import Similar_cos
from sklearn_user.similar_list import Similar_query
from ..models import Maincont,Similar  #점 두개(..)인 이유는 pybo/views/ 두번에 걸쳐서 있음
#기존의 view.py에서 가져옴

def index(request):     #창열어주기

    page = request.GET.get('page', '1')  # 1페이지을 기본으로 출력 > localhost:8000/pybo/?page1
    kw = request.GET.get('kw','')        # localhost:8000/?kw=검색어&page=3
    sr = request.GET.get('sr','recent')  #정렬기준

    if sr =='recommend':  # 추천순
        maincont_list = Maincont.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')

    elif sr =='recent':  # 최신순
        maincont_list = Maincont.objects.order_by('-create_date')  #쿼리셋 형태 : <QuerySer[<Maincont:url>,<Maincont:url>,<Maincont:url>...]>

    elif sr == 'mylist':  # 내가 쓴 글
        maincont_list = Maincont.objects.filter(author__username__icontains=request.user)

    elif sr == 'similar':  #유사성
        similar_q=Similar_query(request.user)
        maincont_list=similar_q.my_similar()




    if kw:                                                      #검색하는 함수
        maincont_list=maincont_list.filter(
            Q(subject__icontains=kw)|     #url로 검색
            Q(word__icontains=kw)|         #단어로 검색
            Q(sentence__icontains=kw)|    #문장으로 검색
            Q(author__username__icontains=kw)       #글쓴이로 검색

        ).distinct()



    #페이징 처리
    paginator = Paginator(maincont_list, 10)    #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)             #페이지 가져오기

    context = {'maincont_list': page_obj, 'page':page, 'kw':kw, 'sr':sr}    #kw(검색어)와 page도 반환
    return render(request, 'pybo/maincont_list.html',context)  #render함수 이용해서 html에 context내용 넣음
    #결과물 : 페이지 1에서 10개의 저장된데이터만 화면에 나타난다.



def detail(request, maincont_id):    #사이트 클릭했을때(id로) 다음창으로 넘어가도록 구현

    maincont=get_object_or_404(Maincont, pk=maincont_id)
    maincont_sentence = Maincont.objects.values_list('sentence')
    maincont_my_sentence = maincont_sentence.filter(
        author__username__icontains=request.user)  # 접속한 유저의 문장들 > 사용자에 따라 request가 바뀌어야됨
    cosine = Similar_cos(maincont.sentence, list(maincont_my_sentence))
    similar_percent = cosine.my_similar()

    # 모델객체 저장 > 중복됨 : 쿼리셋에서 제거
    model_similar=Similar(author=request.user, maincont=maincont, similar=similar_percent)
    model_similar.save()

    context={'maincont':maincont, 'similar_percent':similar_percent}

    return render(request,'pybo/maincont_detail.html',context)


