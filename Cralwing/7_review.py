'''
날짜 : 2021/06/08
이름 : 이진유
내용 : 영화 리뷰 수집하기
'''

from selenium import webdriver
import logging, time

# 로거 생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

# 로그 포맷 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 핸들러 생성
fileHandler = logging.FileHandler('./review.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

# 가상 브라우저 실행(headless 모드로 실행) : gui를 지원하지 않는 서버단에서 실행하기 위해서는 headless  모드로 실행 해줘야 한다.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


browser = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
logger.info('가상 브라우저 실행...')

rank = 0
page = 1
real_rank = 0
while True:

    # 현재 브라우저를 전환
    browser.switch_to.default_content()

    if page > 40:
        break

    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&page=%d' % page)
    logger.info('%d 페이지 이동' % page)
    #browser.switch_to.alert.accept() # Centos8 서버에 올렸을때 오류 발생

    if rank == 49:
        rank = 0
        page += 1

    # 순위별 영화 클릭
    titles = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
    titles[rank].click()
    logger.info('%d위 영화 클릭' % (real_rank + (rank+1)))
    rank += 1



    #영화 제목
    movie_title = browser.find_element_by_css_selector(
    '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    logger.info('%d위 %s 영화 클릭...' % (rank, movie_title))

    # 영화 평점 클릭
    btn_score = browser.find_element_by_css_selector('#movieEndTabMenu > li > a.tab05')
    btn_score.click()

    # 현재 가상 브라우저를 영화 리뷰가 있는 iframe pointAfterListIframe
    browser.switch_to.frame('pointAfterListIframe')

    total_page = int(
        browser.find_element_by_css_selector('body > div > div > div.score_total > strong > em').text.replace(",",
                                                                                                              "")) // 10
    page_count = 0 # 영화 리뷰 페이지
    while True:
        # 영화 리뷰 출력
        lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')

        for li in lis:
            score = li.find_element_by_css_selector('div.star_score > em').text
            reple = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text

            #print(f'{score}, {reple}')

        btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child')
        btn_next.click()
        logger.info('다음 페이지 클릭...')

        page_count += 1
        if page_count > total_page: break

    logger.info('%s 영화 리뷰 수집 완료.....' % movie_title)


