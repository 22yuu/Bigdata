'''
날짜 : 2021/06/07
이름 : 이진유
내용 : 파이썬 HTML 페이지 파싱 실습하기

파싱(Parsing)
 - 문서 해독을 의미
 - 마크업 문서(HTML, XML)에서 특정 태그의 데이터를 추출하는 처리과정
'''

import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청
response = req.get('https://news.naver.com/',
                   headers={'User-Agent':'Mozilla/5.0'}) # 네이버 뉴스의 안티 크롤링 기능을 뚫기 위해 header 정보에 모질라 브라우저의 정보를 가지고 요청한다.
#print(response.text)

# 페이지 파싱
# dom = bs(response.text, 'html.parser') # dom : Document Object Model
# titles = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
#print(titles)

# 파싱 데이터 출력(strip : 공백제거)
# for tit in titles:
#     print(tit.text.strip())


response2 = req.get('https://news.daum.net/ranking/popular', headers={'User-Agent':'Mozilla/5.0'})
dom2 = bs(response2.text, 'html.parser')
titles2 = dom2.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

for i in range(10):
    print(titles2[i].text)
