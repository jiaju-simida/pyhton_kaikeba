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

## 爬取并存储五月天的歌曲信息_对应第七节

```python
from kkb_tools import open_file
import requests
import openpyxl

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
wb=openpyxl.Workbook()
#创建工作薄
sheet=wb.active
#获取工作薄的活动表
sheet.title='songs_mayday'
#工作表重命名
column_name = ['歌曲名','所属专辑','播放时长','播放链接']
sheet.append(column_name)
for x in range(0,3):
    params = {
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
        'p': str(x + 1),
        'n': '20',
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
    # 将参数封装为字典
    res_music = requests.get(url, params=params)
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
        name = music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time = music['interval']
        # 查找播放时长，把时长赋值给time
        link = 'https://y.qq.com/n/yqq/song/' + str(music['file']['media_mid']) + '.html\n\n'
        # 查找播放链接，把链接赋值给link
        sheet.append([name, album, time, link])
        # 把name、album、time和link写成列表，用append函数多行写入Excel

wb.save('mayday.xlsx')
wb.close()
#最后保存并关闭这个Excel文件
open_file('mayday.xlsx')
```

## 第八节
这节内容的爬虫代码已经没用了，被知乎干掉了

## 第九节 cookie

### 存储cookie

```python
import requests
import json
#引入requests和json模块。
session = requests.session()
url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
data = {
    'log': input('请输入你的账号:'),
    'pwd': input('请输入你的密码:'),
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}
session.post(url, headers=headers, data=data)

cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
#把cookie转化成字典。
print(cookie_dict)
#打印cookie_dict
cookie_str = json.dumps(cookie_dict)
#调用json模块的dumps函数，把cookie从字典再转成字符串。
print(cookie_str)
#打印cookie_str
f = open('cookie.txt', 'w')
#创建名为cookie.txt的文件，以写入模式写入内容。
f.write(cookie_str)
#把已经转成字符串的cookie写入文件。
f.close()
#关闭文件。
```

### 读取cookie

```python
import requests

import json

session = requests.session()

headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

}



def cookie_read(): # cookie读取。

    cookie_txt = open('cookie_kaikeba.txt', 'r')

    cookie_dict = json.loads(cookie_txt.read())

    cookie = requests.utils.cookiejar_from_dict(cookie_dict)

    return (cookie)



def sign_in():

    url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'

    data_login = {'log': input('请输入你的账号'),

            'pwd': input('请输入你的密码'),

            'wp-submit': '登录',

            'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',

            'testcookie': '1'}

    session.post(url_login, headers=headers, data=data_login)

    # cookie存储。

    cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)

    cookie_str = json.dumps(cookie_dict)

    f = open('cookie_kaikeba.txt', 'w')

    f.write(cookie_str)

    f.close()



def write_message(): #发表评论。

    url_comment = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'

    data_comment = {

        'comment': input('请输入你要发表的评论：'),

        'submit': '发表评论',

        'comment_post_ID': '35',

        'comment_parent': '0'

    }

    return (session.post(url_comment, headers=headers, data=data_comment))



try:

    session.cookies = cookie_read()

except FileNotFoundError:

    sign_in()

    session.cookies = cookie_read()



num = write_message()

if num.status_code == 200:

    print('成功啦！')

else:

    sign_in()

    session.cookies = cookie_read()

    num = write_message()
```

## 第十节
关于selenium的 跳过

## 定时完成爬取任务_第十一节

```python
import requests

import smtplib

import schedule

import time

from bs4 import BeautifulSoup

from email.mime.text import MIMEText

from email.header import Header



def get_weather():

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

    url = 'http://www.weather.com.cn/weather/101020100.shtml'

    res = requests.get(url, headers=headers)

    res.encoding = 'utf-8'

    bsdata = BeautifulSoup(res.text, 'html.parser')

    data_temperature = bsdata.find(class_='tem')

    data_weather = bsdata.find(class_='wea')

    return data_temperature,data_weather



def send_email(tem,wea,sender,pwd,recevier):

    mailhost='smtp.qq.com'

    qqmail = smtplib.SMTP()

    qqmail.connect(mailhost,25)

    qqmail.login(sender,pwd)

    content= '亲爱的，今天的天气是：'+tem+wea

    message = MIMEText(content, 'plain', 'utf-8')

    subject = '今日天气预报'

    message['Subject'] = Header(subject, 'utf-8')

    try:

        qqmail.sendmail(sender, recevier, message.as_string())

        return True

    except:

        return False

    qqmail.quit()



def job():

    print('开始一次发送任务')

    tem,wea = get_weather() 

    IsSuccess = send_email(tem,wea,sender,pwd,recevier) # 这里需要设置发件人的账号密码以及收件人的账号

    while IsSuccess is False:

        print("邮件发送失败，正在尝试重新发送")

        IsSuccess = send_email(tem, wea, sender, pwd, recevier)

    print('任务完成')



schedule.every().day.at("07:30").do(job)

while True:

    schedule.run_pending()

    time.sleep(1)
```

## 异步爬取_第十二节

```python
from gevent import monkey

monkey.patch_all()

#从gevent库里导入monkey模块

import gevent

import time

import requests

from gevent.queue import Queue
monkey.patch_all()

#从gevent库里导入queue模块


#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。

start = time.time()



url_list = ['https://www.baidu.com/',

'https://www.sina.com.cn/',

'http://www.sohu.com/',

'https://www.qq.com/',

'https://www.163.com/',

'http://www.iqiyi.com/',

'https://www.tmall.com/',

'http://www.ifeng.com/']



work = Queue()

#创建队列对象，并赋值给work

for url in url_list:

#遍历url_list

    work.put_nowait(url)

    #用put_nowait()函数可以把网址都放进队列里



def crawler():

    while not work.empty():

    #当队列不是空的时候，就执行下面的程序

        url = work.get_nowait()

        #用get_nowait()函数可以把队列里的网址都取出

        r = requests.get(url)

        #用requests.get()函数抓取网址

        print(url,work.qsize(),r.status_code)

        #打印网址、队列长度、抓取请求的状态码



tasks_list  = [ ]

#创建空的任务列表

for x in range(2):

#相当于创建了2个爬虫

    task = gevent.spawn(crawler)

    #用gevent.spawn()函数创建执行crawler()函数的任务

    tasks_list.append(task)

    #往任务列表添加任务。

gevent.joinall(tasks_list)

#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站

end = time.time()

print(end-start)
```

## 爬取食物热量_第十三节

```python
# 导入所需的库和模块：
from gevent import monkey
import gevent,requests,bs4,openpyxl,time
from gevent.queue import Queue
from openpyxl import load_workbook,Workbook,worksheet

#让程序变成异步模式
monkey.patch_all()
# 创建队列对象，并赋值给work
work = Queue()

# 前3个分类的前3页的食物记录的网址：
url_1 = "https://food.hiyd.com/list-{type}-html?page={page}"
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)
# 通过两个for循环，能设置分类的数字和页数的数字
# 然后，把构造好的网址用put_nowait方法添加进队列里

# 第11个分类的前3页的食物记录的网址：
url_2 = "https://food.hiyd.com/list-132-html?page={page}"
for x in range(1, 4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)
# 通过for循环，能设置第11个常见食物分类的食物的页数。
# 然后，把构造好的网址用put_nowait方法添加进队列里。

print(work)
# 打印队列

def crawler(job):# 定义crawler函数
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    # 添加请求头
    while not job.empty():
        # 当队列不是空的时候，就执行下面的程序
        url = job.get_nowait()
        # 用get_nowait()方法从队列里把刚刚放入的网址提取出来
        res = requests.get(url, headers=headers)
        # 用requests.get获取网页源代码
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        # 用BeautifulSoup解析网页源代码
        category = bs_res.find('b').text
        # 用find提取出<b>标签的内容,当前页面所属的分类
        foods = bs_res.find_all('li')
        # 用find_all提取出<li>标签的内容
        result_list = []
        # 创建空的list用来存储结果
        for food in foods:# 遍历foods
            food_name = food.find('a').find_all('div')[1].find('h3').text
            # 用find_all在<li>标签下，提取出第二个<div>标签中<h3>标签中的文本，也就是食物名称
            food_calorie = food.find('a').find_all('div')[1].find('p').text
            # 用find_all在<li>标签下，提取出第二个<div>标签中<p>标签中的文本，也就是食物热量
            food_url = 'http:' + food.find('a')['href']
            # 用find_all在<li>标签下，提取出唯一一个<a>标签中href属性的值，跟'http:'组合在一起，就是食物详情页的链接
            print([category, food_name, food_calorie, food_url])
            # 打印食物的名称    
            result_list.append([category, food_name, food_calorie, food_url])

        savedata(result_list)

def savedata(li): #定义写入数据的函数
    try:
        wb = load_workbook("result.xlsx")
    except:
        wb = Workbook()
    finally:
        try:
            ws = wb[li[0][0]] #若工作表不存在就创建一个当前类别命名的工作表
        except Exception as e:
            ws = wb.create_sheet(li[0][0],index=0)
            ws.append(["类别","食物名称","热量","链接"])
        finally:
            for x in li:
                ws.append(x) # 按行写入数据
    wb.save("result.xlsx")
    wb.close()

tasks_list = []
# 创建空的任务列表
for x in range(5):
    # 相当于创建了5个爬虫
    task = gevent.spawn(crawler(work))
    # 用gevent.spawn()函数创建执行crawler()函数的任务
    tasks_list.append(task)
    # 往任务列表添加任务
gevent.joinall(tasks_list)
# 用gevent.joinall方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站
```
