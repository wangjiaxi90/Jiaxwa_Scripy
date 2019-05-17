import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

BASE_URL = 'https://freemidi.org/'
pa = r'C:\Users\v-jiaxwa\Desktop\4\rock\\'
genres = ['genre-rock']  # , 'genre-pop', 'genre-dance-eletric', 'genre-jazz']
for genre in genres:
    url = BASE_URL + genre
    folder_name = pa + genre
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    session = requests.Session()
    html = session.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    genre_links = soup.select(".genre-link-text > a")
    for genre_link in genre_links:
        artist_id = genre_link['href']
        artist_name = genre_link.text.strip()
        artist_url = BASE_URL + artist_id
        html = session.get(artist_url).content
        soup = BeautifulSoup(html, 'lxml')
        artist_links = soup.select('.artist-song-cell a')
        for artist_link in artist_links:
            song_url = BASE_URL + artist_link['href']
            song_id = song_url.split('-')[1]
            song_name = artist_link.text.strip()
            song_path = f'{artist_name} - {song_name}'.replace('/', ' ').replace('\t', ' ')
            file_name = f'{folder_name}/{song_path}.mid'
            if not os.path.isfile(file_name):
                print(file_name)
                session.get(song_url)
                download_url = BASE_URL + 'getter-' + song_id
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
                headers.update({"Referer": song_url})
                r = session.get(download_url, headers=headers)
                with open(file_name, 'wb') as f:
                    f.write(r.content)

# # !/usr/bin/python
# # encoding: UTF-8
# import re
# import requests
# import os
# import urllib.request
#
# url = 'https://freemidi.org/getter-13560'
# path = r'C:\Users\v-jiaxwa\Desktop\pachong3.7\testtttt.midi'
# urllib.request.urlretrieve(url, path)
# # r = requests.get(url, stream=True)
# # f = open("file_path.midi", "wb")
# # # chunk是指定每次写入的大小，每次只写了512byte
# # for chunk in r.iter_content(chunk_size=512):
# #     if chunk:
# #         f.write(chunk)
# print("Done")
#
# # f = open(r'\\stcav-526\submit\2019-4-26-ToPeiling-Pachong\freemidi\pop\TimeOfTheSeason.mid', 'rb')
# # content= f.read()
# # print(content)
# # f.close()
#
#
# # # make English text clean
# # def clean_en_text(text):
# #     # keep English, digital and space
# #     comp = re.compile('[^A-Z^a-z^0-9^ ]')
# #     return comp.sub('', text)
# #
# #
# # # make Chinese text clean
# # def clean_zh_text(text):
# #     # keep English, digital and Chinese
# #     comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
# #     return comp.sub('', text)
# #
# #
# # if __name__ == '__main__':
# #     a = 'aaaa__s++dsa2'
# #     b = clean_en_text(a)
# #     print(b)
#     # text_en = '$How old are you? Could you give me your pen?'
#     # text_zh = '$你好！我是个程序猿，标注码农￥'
#     # print(clean_en_text(text_en))
#     # print(clean_zh_text(text_zh))
