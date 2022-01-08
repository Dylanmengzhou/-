## 网易云推荐专辑爬取

注：此项目为教育意义，所有版权归网易云所有


此项目有两个文件
#### RequestURL.py
#### 获取.py


### 1. RequeestURL
这是一个个性化module 用request改的，主要目的是为了能判断服务器返回的html是需要headers并且判断原文是否包含特定字段

#### RequestPackage
import request


#### 解释：
参数：
1. url
2. headers（默认none）
3. encode （默认：'utf-8'）
4. check_string（默认："headers"）

返回：
如正确返回：return request.get()
如不正确返回：return None
  1. 没有添加headers：print('Request Headers, Please input headers')
  2. 状态码正常但是缺少字段：print('status 200 with headers, but not full html')


### 2. 获取
#### RequestPackage

1. import requests
2. import os
3. from lxml import etree
4. from RequestURL import request_web
5. import re

#### 解释
1. 获取源html
2. 用xpath在总专辑中获取名字以及每个专辑的id
3. 根据baseurl+特定的专辑id 获取每个页面的url的源html
4. 用re获取每个专辑里边的歌曲名字以及id，并建立专辑文件在本地
5. 根据baseurl+特定歌曲的id，用request.get()获取每个歌曲
6. 分别保存在每个专辑文件中，并将所有文件保存在 # music/ 文件下

总专辑url：http://music.163.com/discover/playlist
此url是http协议，因为原网站是：https://music.163.com/#/discover/playlist
当我用request.get()方法获取时返回的是登陆页面

专辑baseurl：http://music.163.com/playlist?id=
单个歌曲baseurl：http://music.163.com/song/media/outer/url?id=







