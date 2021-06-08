'''
날짜 : 2021/06/07
이름 : 이진유
내용 : 파이썬 실시간 검색어 크롤링 실습

zum 사이트 실시간 검색어 크롤링

'''

import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import os

response = req.get('https://issue.zum.com/')
# print(response.text)

# 페이지 파싱하기
dom = bs(response.text, 'html.parser')
lis = dom.select('#issueKeywordOpenList > li')

# 쌤 코드
# dom = bs(response.text, "html.parser")
# divs = dom.select('#issueKeywordOpenList > li > div.cont')
# for div in divs:
#     rank = div.find(class='num')
#     word = div.find(class='word')
#     print('%s, %s' %(rank, word))

dir = './keyword/{:%Y-%M-%d}'.format(datetime.now())

# 디렉터리 생성
if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 생성
fname = '{:%Y-%M-%d-%H-%M}.txt'.format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')


print('순위 검색어')
for li in lis:
    spans = li.find_all('span')
    print(f'{spans[0].text[:-1]},{spans[2].text}')
    file.write('{},{}\n'.format(spans[0].text[:-1] if spans[0].text.strip() else 'NA',
                                spans[2].text if spans[0].text.strip() else 'NA'))
file.close()

print('실시간 검색어 수집 완료...')