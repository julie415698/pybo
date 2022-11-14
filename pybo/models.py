from django.db import models
from django.contrib.auth.models import User  #계정 연결
#models.py는 전체적인 틀(구성), forms.py는 입력하는 객체
from textrank.textrank import TextRank  #textrank 함수 호출


class Maincont(models.Model):

    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_maincont')  #계정이 삭제되면 관련데이터 삭제 / author 추가

    modify_date = models.DateTimeField(null=True, blank=True)  #데이터 수정일시 의미 (값을 비워두어도된다)

    subject=models.TextField() #url필드는 글자수 제한있음( urlfield() )
    sentence =models.TextField(blank=True) #요약문장  - blank=True 값이 비어있어도 허용
    word = models.TextField(blank=True)   #요약단어   - blank=True 값이 비어있어도 허용

    create_date=models.DateTimeField()#작성날짜

    voter=models.ManyToManyField(User, related_name='voter_maincont') #게시글 추천기능
   #연관도를 model객체에서 없앤다

    def __str__(self):
        return self.subject     #출력시 제목표시


class Comment(models.Model):                                    #댓글 모델
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    maincont=models.ForeignKey(Maincont, null=True, blank=True, on_delete=models.CASCADE) #이 댓글이 달린 게시글 / on_delete : subject삭제시 같이 삭제


class Similar(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)   #request.user
    maincont=models.ForeignKey(Maincont, null=True, blank=True, on_delete=models.CASCADE)  # 이 유사도에 해당하는 게시글
    similar=models.IntegerField(default=0)  #유사도


# Create your models here.
