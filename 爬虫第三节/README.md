# 爬虫第三节

***

爬取的网站不知道后面会不会过期 仅供参考

爬取网站为[开课吧食堂](https://xiaoke.kaikeba.com/example/canteen/index.html)

## BeautifulSoup基础

### BeautifulSoup解析网页

```python
import requests
from bs4 import BeautifulSoup
#引入BS库
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象
```

###  BeautifulSoup对象的find与find_all方法

find与find_all的参数为(标签,属性)

这俩个方法返回的是一个**tag**类型数据

**tag对象也有find与find_all**

**tag.['something'] 提取tag中的something属性值**

```python
import requests
from bs4 import BeautifulSoup
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get (url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
item = soup.find('div') #使用find()方法提取首个<div>元素，并放到变量item里。
item = soup.find_all('div') #使用find_all()方法提取所有<div>元素，并放到变量item里。
print(type(item)) #打印item的数据类型
print(item) #打印itemxa0
```
