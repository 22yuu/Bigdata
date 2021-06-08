'''
날짜 : 2021/06/08
이름 : 이진유
내용 : 가상 브라우저를 활용한 날씨 데이터 크롤링 실습

seleninum와 bs4의 차이는

동적과 정적?

selenium은 동적으로 페이지를 생성, bs4는 정적 페이지
'''

from selenium import webdriver

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 페이지 파싱
trs = browser.find_elements_by_css_selector('#weather_table > tbody > tr')

for tr in trs:
    local = tr.find_element_by_css_selector('td:nth-child(1) > a').text
    temp = tr.find_element_by_css_selector('td:nth-child(6)').text

    print(f'{local}, {temp}')

browser.close()