#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
# 定义请求头(第六课会讲到)
res_movies = requests.get('https://movie.douban.com/chart',headers=headers)
# 获取数据,传入参数,第一个是url,第二个是请求头
bs_movies = BeautifulSoup(res_movies.text,'html.parser')
# 解析数据

tag_name = bs_movies.find_all('div', class_='pl2')
# 查找包含电影名和电影详情URL的<div>标签，这里<a>标签没有明显的属性，我们找到了它的上一级标签
tag_p = bs_movies.find_all('p',class_='pl')
# 查找包含电影基本信息的<p>标签
tag_div = bs_movies.find_all('div', class_='star clearfix')
# 查找包含电影评分信息的<div>标签
list_all = []
# 创建一个空列表，用于存储信息
for x in range(len(tag_name)):
# 启动一个循环，次数等于电影名的数量
    list_movie = [tag_name[x].find('a').text.replace(' ', '').replace('\n', ''),tag_name[x].find('a')['href'],tag_p[x].text.replace(' ', '').replace('\n', ''),tag_div[x].text.replace(' ', '').replace('\n', '')]
# 提取信息，封装为列表。
    list_all.append(list_movie)
# 将信息添加进list_all
print(list_all)
# 打印


# In[ ]:




