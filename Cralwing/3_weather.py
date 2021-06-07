'''
날짜 : 2021/06/07
이름 : 이진유
내용 : 파이썬 전국 날씨 데이터 크롤링 실습하기
'''

import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import os

response = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
# print(response.text)

# 데이터 출력
# #weather_table > tbody > tr:nth-child(1) > td:nth-child(1)

dom = bs(response.text, 'html.parser')
locs = dom.select('#weather_table > tbody > tr > td:nth-child(1)')
temps = dom.select('#weather_table > tbody > tr > td:nth-child(6)')
trs = dom.select('#weather_table > tbody > tr')

# for i in range(10):
#     print(f'지역명 : {locs[i].text}, 온도 : {temps[i].text}')

# 디렉터리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    # 현재 디렉터리 존재하지 않는다면
    os.makedirs(dir)

# 데이터 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 데이터 파일 저장
file.write('지역,현재일기,시정,운량,중하운량,현재기온,이슬점온도,불쾌지수,일강수,습도,풍향,풍속,해면기압\n')


for i, tr in enumerate(trs):
    tds = tr.find_all('td')
    #print(f'{i+1}. 지역명 : {tds[0].text}, 온도 : {tds[5].text}')
    file.write("{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(tds[0].text,
                                                                  tds[1].text,
                                                                  tds[2].text,
                                                                  tds[3].text,
                                                                  tds[4].text,
                                                                  tds[5].text,
                                                                  tds[6].text,
                                                                  tds[7].text,
                                                                  tds[8].text,
                                                                  tds[9].text,
                                                                  tds[10].text,
                                                                  tds[11].text,
                                                                  tds[12].text))
file.close()
print('날씨 데이터 수집완료...')

