#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:




