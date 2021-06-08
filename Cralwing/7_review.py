'''
날짜 : 2021/06/08
이름 : 이진유
내용 : 영화 리뷰 수집하기
'''

from selenium import webdriver


# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 이동
browser.get('https://movie.naver.com/')

# 영화 랭킹 클릭
btn_rank = browser.find_element_by_css_selector('#scrollbar > div.scrollbar-box > div > div > ul > li:nth-child(3) > a')
btn_rank.click()

# 평점순 클릭
btn_score = browser.find_element_by_css_selector('#old_content > div.tab_type_6 > ul > li:nth-child(3) > a')
btn_score.click()


# 순위별 영화 클릭
titles = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
titles[0].click()

# 영화 평점 클릭
btn_score = browser.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(5) > a')
btn_score.click()

# 현재 가상 브라우저를 영화 리뷰가 있는 iframe pointAfterListIframe
browser.switch_to.frame('pointAfterListIframe')

total_page = int(
    browser.find_element_by_css_selector('body > div > div > div.score_total > strong > em').text.replace(",",
                                                                                                          "")) // 10
page_count = 0
while True:
    # 영화 리뷰 출력
    lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')

    for li in lis:
        score = li.find_element_by_css_selector('div.star_score > em').text
        reple = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text

        print(f'{score}, {reple}')

    btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child')
    btn_next.click()

    page_count+=1

    if page_count > total_page: break

# while True:
#     # 영화 리뷰 출력
#     lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')
#
#     # #_filtered_ment_0
#
#     for li in lis:
#         score = li.find_element_by_css_selector('div.star_score > em').text
#         reple = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text
#
#         print(f'{score}, {reple}')
#
#     btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child')
#     btn_next.click()

print('네이버 영화 리뷰 수집 종료...')


