'''
날짜 : 2021/06/07
이름 : 이진유
내용 : 파이썬 웹 Request 실습하기
'''

import requests as req

# 네이버 페이지 요청
response = req.get('http://naver.com')
print(response.text)



