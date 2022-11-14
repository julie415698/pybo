from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

import kss


def getsummarize(txt):
    txt = txt.replace("\n", ' ')
    sents = ""

    for sent in kss.split_sentences(txt):
        sents = sents + sent + "\n"

    summaries = summarize(sents, word_count=150, split=True)

    return summaries


def getkeyword(txt):
    txt = txt.replace("\n", ' ')
    sents = ""

    for sent in kss.split_sentences(txt):
        sents = sents + sent + "\n"

    return keywords(sents).split("\n")


if __name__ == "__main__":
    txt = '''11월 수출액이 사상 처음으로 600억 달러를 돌파했습니다. 이전 최고 수출액은 올 9월의 559억 2000만 달러였습니다. 두 달 만에 최고 기록을 경신하며 가파른 증가세를 보인 것입니다. 산업통상자원부가 발표한 11월 수출입 동향에 따르면 이달 수출은 604억 4000만 달러로 전년 동월 대비 32.1% 증가했습니다.  수입은 43.6% 늘어난 573억 6000만 달러, 무역수지는 30억 9000만 달러 흑자를 기록했습니다. 무역수지 흑자는 19개월 연속 이어졌습니다. 1월 수출의 주요 특징을 살펴보면 우선, 수출액이 대한민국 무역 역사상 최초로 600억 달러를 돌파했다는 것입니다. 지난 2013년 10월 500억 달러 진입 이후 8년 1개월 만에 600억 달러 대로 올라선 것입니다. 올 7월 이후 월평균 수출액도 550억 달러로 성장했습니다. 또한 수출은 13개월 연속 증가했습니다. 작년 11월 전년 동월 대비 3.9% 증가하며 연속의 첫 발을 내디딘 이후 코로나19 기저효과가 없음에도 30%대 고성장을 이뤘습니다. 수출 물량과 단가도 각각 8.2%와 22.1% 늘어 2개월 연속 동시 증가했습니다. 품목별 수출 동향을 보면 15대 주요 품목 중 13개 품목이 증가했습니다. 다만 차량용 반도체 수급 문제로 글로벌 자동차 생산에 차질이 빚어지면서 차부품이 소폭 감소했고, 바이오헬스는 역대 4위의 수출액에도 작년 11월의 높은 실적(역대 3위)에 따른 기저효과로 줄었습니다. 이밖에 사상 최초로 8개월 연속 9대 지역으로의 수출이 모두 늘었습니다. 특히 중국과 아세안으로의 수출은 월 기준 역대 최고치를 기록했습니다. 중국 수출은 사상 첫 150억달러 상회, 아세안 수출은 최초로 100억달러를 돌파한 것입니다. 이에 따라 올해는 사상 최대 수출과 무역 규모를 달성할 전망입니다. 1~11월 누적 수출액은 5838억달러, 무역액은 1조 1375억달러입니다.'''

    print(getsummarize(txt))
    print(getkeyword(txt))