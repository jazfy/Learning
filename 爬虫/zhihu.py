import requests
from pyquery import PyQuery as pq #解析库

url = 'https://www.zhihu.com/explore'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.2 Safari/537.36'
}

html = requests.get(url,headers=headers).text #得到解析页面
doc = pq(html) #开始解析

items = doc(' .explore-tab .feed-item').items()

for item in items: #遍历提取相关内容
    question = item.find('h2').text() #问题部分
    author = item.find('.author-link-line').text() #作者信息
    answer = pq(item.find('.content').html().text() #正文
    #files = open('explore.txt','a+',) #规定写入内容格式

    with open('explore.txt','a',encoding='utf-8') as files: #不知为何,无法保存 
        files.write('\n'.join([question,author,answer])) #规定写入内容
        files.write('\n' + '=' * 50 + '\n') #写入具体格式
        files.close()