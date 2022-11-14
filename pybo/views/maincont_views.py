#게시글 관리 (생성 , 수정 , 삭제)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, redirect
from django.utils import timezone
from newspaper import Article

from sklearn_user.similar_cosine import Similar_cos
from textrank.textrank import TextRank  #텍스트랭크 함수 호출
from ..forms import MaincontForm
from ..models import Maincont

#여기에 텍스트링크를 객체와 연결 해야됨
@login_required(login_url='common:login') # 웹활동전에 로그인 여부 검사 , 만일 안돼있으면 로그인 창으로 넘어감
def maincont_create(request):
    if request.method == 'POST':       #데이터 저장
        form = MaincontForm(request.POST)
        if form.is_valid()  :         #폼이 유효한지'''
            maincont = form.save(commit=False)    #데이터 False:임시저장                         #<게시글작성>

            # textrank 함수 가져옴
            url = maincont.subject  # url을 웹으로 부터 받아옴

            sen_list = []  # 문장 리스트 생성
            wor_list = []  # 단어 리스트 생성

            textrank = TextRank(url)

            for sen in textrank.summarize(3):  # 문장 1개 리턴 > 요약문장 3개
                sen_list.append(sen + '\n')

            maincont.sentence = "".join(sen_list)

            for wor in textrank.keywords(3):  # 단어 1개 리턴 > 요약단어 3개
                wor_list.append('#' + wor + '')

            maincont.word = "".join(wor_list)

            # textrank 함수 끝


            maincont.author = request.user     #추가한 author속성 적용 (추가)
            maincont.create_date = timezone.now()  #날짜 받아옴
            maincont.save()                        #데이터 완전저장
            return redirect('pybo:index')   #index 화면으로 돌아감

    else:       #request.method =='GET' / 추가등록 버튼클릭
        form=MaincontForm()

    context = {'form' : form}
    return render(request, 'pybo/maincont_form.html',context)    #폼 객체 띄워줌


@login_required(login_url='common:login')
def maincont_modify(request, maincont_id):
    maincont = get_object_or_404(Maincont, pk=maincont_id)                                #<게시글 수정>

    if request.user != maincont.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', maincont_id=maincont_id)

    if request.method == "POST":
        form=MaincontForm(request.POST, instance=maincont) # instance=maincont:기존저장상태에서 수정 / request.POST:수정함 (덮어씌움)
        if form.is_valid():
            maincont=form.save(commit=False)  #폼 임시 저장 1
            maincont.author=request.user      #사용자 같은지 확인 2
            maincont.modify_date=timezone.now() #수정일시 저장
            maincont.save()                     # 2확인 했으니 1을 영구저장으로바꿈
            return redirect('pybo:detail', maincont_id=maincont.id)    #수정하기 버튼 누르면 detail.html로 돌아감 , index.html 아님

    else:
        form=MaincontForm(instance=maincont)

    context={'form' : form}
    return render(request, 'pybo/maincont_form.html',context)

@login_required(login_url='common:login')
def maincont_delete(request , maincont_id):
    maincont=get_object_or_404(Maincont, pk=maincont_id)                        #<게시글 삭제기능>
    if request.user != maincont.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', maincont_id=maincont.id)
    else:
        maincont.delete()
    return redirect('pybo:index')

