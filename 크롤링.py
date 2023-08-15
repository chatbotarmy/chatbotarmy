pip install beautifulsoup4
pip install requests


import requests
from bs4 import BeautifulSoup

def naver_news_crawler(keyword, num_pages=1):
    base_url = 'https://search.naver.com/search.naver'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    news_titles = []

    for page in range(1, num_pages + 1):
        params = {
            'where': 'news',
            'query': keyword,
            'start': (page - 1) * 10 + 1,
        }
        response = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        news_items = soup.select('.list_news .news_wrap .news_area')
        for item in news_items:
            title = item.select_one('.news_tit').text
            news_titles.append(title)

    return news_titles

if __name__ == '__main__':
    keyword = '인공지능'
    num_pages = 2  # 크롤링할 페이지 수 (한 페이지 당 10개의 뉴스 제목)
    result = naver_news_crawler(keyword, num_pages)
    for idx, title in enumerate(result, 1):
        print(f"{idx}. {title}")
