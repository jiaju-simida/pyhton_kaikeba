# pyhton_kaikeba
开课吧坑壁python课爬虫代码备份

## 菜谱爬虫_对应第三节

```python
import requests
from bs4 import BeautifulSoup
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser') 
items = soup.find_all(class_='show-list-item')
for item in items: 
    title = item.find(class_='desc-title') # 在列表中的每个元素里，匹配属性class_='title'提取出数据
    material = item.find(class_='desc-material') #在列表中的每个元素里，匹配属性class_='desc-material'提取出数据
    step = item.find(class_='desc-step') #在列表中的每个元素里，匹配属性class_='desc-step'提取出数据
    print(title.text,material.text,step.text)
```

## 豆瓣新片榜_对应第四节

```python
import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
res_movies = requests.get('https://movie.douban.com/chart',headers=headers)
# 获取数据
bs_movies = BeautifulSoup(res_movies.text,'html.parser')
# 解析数据
list_movies= bs_movies.find_all('div',class_='pl2')
# 查找最小父级标签

list_all = []
# 创建一个空列表，用于存储信息

for movie in list_movies:
    tag_a = movie.find('a')
# 提取第1个父级标签中的<a>标签
    name = tag_a.text.replace(' ', '').replace('\n', '')
# 电影名，使用replace方法去掉多余的空格及换行符
    url = tag_a['href']
# 电影详情页的链接
    tag_p = movie.find('p', class_='pl')
# 提取第1个父级标签中的<p>标签
    information = tag_p.text.replace(' ', '').replace('\n', '')
# 电影基本信息，使用replace方法去掉多余的空格及换行符
    tag_div = movie.find('div', class_='star clearfix')
# 提取第1个父级标签中的<div>标签
    rating = tag_div.text.replace(' ', '').replace('\n', '')
# 电影评分信息，使用replace方法去掉多余的空格及换行符
    list_all.append([name,url,information,rating])
# 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all

print(list_all)
# 打印
```

## 爬取五月天歌单_对应第五节

```python
import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
res_movies = requests.get('https://movie.douban.com/chart',headers=headers)
# 获取数据
bs_movies = BeautifulSoup(res_movies.text,'html.parser')
# 解析数据
list_movies= bs_movies.find_all('div',class_='pl2')
# 查找最小父级标签

list_all = []
# 创建一个空列表，用于存储信息

for movie in list_movies:
    tag_a = movie.find('a')
# 提取第1个父级标签中的<a>标签
    name = tag_a.text.replace(' ', '').replace('\n', '')
# 电影名，使用replace方法去掉多余的空格及换行符
    url = tag_a['href']
# 电影详情页的链接
    tag_p = movie.find('p', class_='pl')
# 提取第1个父级标签中的<p>标签
    information = tag_p.text.replace(' ', '').replace('\n', '')
# 电影基本信息，使用replace方法去掉多余的空格及换行符
    tag_div = movie.find('div', class_='star clearfix')
# 提取第1个父级标签中的<div>标签
    rating = tag_div.text.replace(' ', '').replace('\n', '')
# 电影评分信息，使用replace方法去掉多余的空格及换行符
    list_all.append([name,url,information,rating])
# 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all

print(list_all)
# 打印
```

## 爬取五月天全部歌单_对应第六节

```python
import requests

# 引用requests模块

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for x in range(1,4):

    param = {

        'ct': '24',

        'qqmusic_ver': '1298',

        'new_json': '1',

        'remoteplace': 'sizer.yqq.song_next',

        'searchid': '64405487069162918',

        't': '0',

        'aggr': '1',

        'cr': '1',

        'catZhida': '1',

        'lossless': '0',

        'flag_qc': '0',

        'p': x,

        'n': '40',

        'w': '五月天',

        'g_tk': '5381',

        'loginUin': '0',

        'hostUin': '0',

        'format': 'json',

        'inCharset': 'utf8',

        'outCharset': 'utf-8',

        'notice': '0',

        'platform': 'yqq.json',

        'needNewCode': '0'

    }

    res_songs= requests.get(url, params=param, headers=headers)

    # 调用get方法，下载歌曲清单

    json_songs = res_songs.json()

    # 使用json()方法，将response对象，转为列表/字典

    # print(json_movie)

    list_songs = json_songs['data']['song']['list']

    for song in list_songs:

        print(x,song['name'])

    #输出的时候标记歌曲所在的页码
```
