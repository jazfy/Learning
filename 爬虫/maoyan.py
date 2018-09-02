# 抓取首页

import requests

def get_one_page(url):
    headers = {
        'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'
    }
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        return r.text
    return None

def main():
    url = 'http://maoyan.com/board/4?offset=0'
    html = get_one_page(url)
    print(html)

main()