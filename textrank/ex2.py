#텍스트랭트 패키지를 이용
from textrank import TextRank
from newspaper import Article

article = Article("https://a-littlecoding.tistory.com/27")
article.download()
article.parse()

print("제목",article.title)
print("전체 내용",article.text)
print('\n')
#print(type(article.text))   #Article()은 str이 타입이다.


string_all = article.text
textrank = TextRank(string_all)
print("요약내용")
print('\n')
print( textrank.summarize(3) ) #3문장으로 요약 > 불용어 재거 해줘야될듯
