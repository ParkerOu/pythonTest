#包含:日期 作者 標題 內文 看板名稱
import requests
import re
from bs4 import BeautifulSoup

def get_total_page_cnt(HomeURL):
    # HomeURL = "https://www.ptt.cc/bbs/Gossiping/index.html"

    custom_headers = {
        "cookie": "over18=1;"
    }

    resp = requests.get(HomeURL, headers=custom_headers)

    # ‹-> &lsaquo;
    total_page_cnt = int(re.findall('href="/bbs/\w+/index(\d+).html">&lsaquo; 上頁', resp.text)[0]) + 1
    return total_page_cnt

# get_total_page_cnt("https://www.ptt.cc/bbs/Gossiping/index.html")


def get_list_page(url):
    # 爬取PTT列表頁面
    HOST = "https://www.ptt.cc"

    custom_headers = {
        "cookie": "over18=1;"
    }

    resp = requests.get(url, headers=custom_headers)
    links = re.findall('<a href="(/bbs/Gossiping/M.+\.html)">.+</a>', resp.text)
    detail_page_links = [HOST + link for link in links]
    return detail_page_links

# get_list_page("https://www.ptt.cc/bbs/Gossiping/index39350.html")


def get_page_content(url):
    custom_headers = {
    "cookie": "over18=1;"
    }

    resp = requests.get(url, headers=custom_headers)

    # author board title pub_date
    soup = BeautifulSoup(resp.text, 'lxml')
    metas = [tag.text for tag in soup.select('.article-meta-value')]

    page = {}
    page['author']   = metas[0]
    page['board']    = metas[1]
    page['title']    = metas[2]
    page['pub_date'] = metas[3]

    # content
    content = soup.select_one('div#main-content')
    selectors_to_del = ['.article-metaline',
                       '.article-metaline-right',
                        'span.f2',
                        'div.push'
                       ]

    for selector in selectors_to_del:
        [tag.extract() for tag in content.select(selector)]

    page['content'] = content.text.strip()

    return page

# get_page_content("https://www.ptt.cc/bbs/Gossiping/M.1535597884.A.23E.html")