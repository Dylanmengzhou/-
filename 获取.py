import fileinput

import requests
import os
from lxml import etree
from RequestURL import request_web
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

music_list_total_url = 'http://music.163.com/discover/playlist'

res = request_web(url=music_list_total_url, headers=headers, encode='utf-8', check_string='初听不知曲中意，再听已是曲中人')
base_url = "http://music.163.com/playlist?id="

id = re.compile(r"\d+")
song = re.compile(r'<li><a href="/song?id=1455273374">风的小径</a></li>')
html = etree.HTML(res.text)
all_li = html.xpath("/html/body/div[3]/div/ul/li")
music_list_url = []
music_list_name = []

all_music_folder_name = 'music/'
if not os.path.exists(all_music_folder_name):
    os.mkdir(all_music_folder_name)
for single_li in all_li:
    list_name = single_li.xpath("./p[1]/a/text()")[0]
    list_id = single_li.xpath("./p[1]/a/@href")[0]
    list_id = re.search(id, list_id).group()
    music_list_name.append(list_name)
    music_list_url.append(base_url + list_id)
for single_list_url in range(0,len(music_list_url)):
    result = requests.get(url=music_list_url[single_list_url], headers=headers)
    result.encoding = 'utf-8'
    song = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a></li>', result.text)
    list_folder_name = r'{}/'.format(music_list_name[single_list_url]).replace('/','-')

    try:

        os.mkdir(os.path.join(all_music_folder_name, list_folder_name))
    except:
        list_folder_name = r'{}(2)/'.format(music_list_name[single_list_url]).replace('/','-')
        os.mkdir(os.path.join(all_music_folder_name, list_folder_name))

    print('正在写入 (------{}------) 文件中......'.format(list_folder_name))
    for song_id, song_name in song:
        single_music_url = f'http://music.163.com/song/media/outer/url?id={song_id}.mp3'
        single_music_content = requests.get(url=single_music_url, headers=headers).content
        with open('music/'+list_folder_name+'/'+str(song_name).replace('/','-')+ '.mp3', mode='wb') as f:
            f.write(single_music_content)
        f.close()
    print('写入 (------{}------) 文件已完成!\n'.format(list_folder_name))