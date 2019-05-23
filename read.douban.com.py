import re
import requests
from lxml import etree
import os
from usedaili import GetHtml
import json

# https://read.douban.com/category/?kind/100  小说
# https://read.douban.com/category/?kind/101 文学
# https://read.douban.com/category/?kind/102 人文社科
# https://read.douban.com/category/?kind/103 经济管理
# https://read.douban.com/category/?kind/104 科技科普
# https://read.douban.com/category/?kind/105 计算机与互联网
# https://read.douban.com/category/?kind/106 成功励志
# https://read.douban.com/category/?kind/107 生活
# https://read.douban.com/category/?kind/108 少儿
# https://read.douban.com/category/?kind/109 艺术设计
# https://read.douban.com/category/?kind/110 漫画绘本
# https://read.douban.com/category/?kind/111 教育考试
# https://read.douban.com/category/?kind/2   杂志
url_ls = {"小说": "https://read.douban.com/category/?kind/100",
          "文学": "https://read.douban.com/category/?kind/101",
          "人文社科": "https://read.douban.com/category/?kind/102",
          "经济管理": "https://read.douban.com/category/?kind/103",
          "科技科普": "https://read.douban.com/category/?kind/104",
          "计算机与互联网": "https://read.douban.com/category/?kind/105",
          "成功励志": "https://read.douban.com/category/?kind/106",
          "生活": "https://read.douban.com/category/?kind/107",
          "少儿": "https://read.douban.com/category/?kind/108",
          "艺术设计": "https://read.douban.com/category/?kind/109",
          "漫画绘本": "https://read.douban.com/category/?kind/110",
          "教育考试": "https://read.douban.com/category/?kind/111",
          "杂志": "https://read.douban.com/category/?kind/2"
          }
base_path = r'C:\Users\v-jiaxwa\Desktop\4'
dl_request = GetHtml()
domain = "https://read.douban.com"
for folder_name in url_ls.keys():
    # 设置基目录
    path = os.path.join(base_path, folder_name)

    title_f = os.path.join(path, 'title.txt')
    description2_f = os.path.join(path, 'description2.txt')
    comment_f = os.path.join(path, 'comment.txt')
    json_f = os.path.join(path, 'json.txt')

    # 创建目录和文件
    if not os.path.exists(path):
        os.makedirs(path)
        # os.mkfifo(title_f)
        # os.mkfifo(description2_f)
        # os.mkfifo(comment_f)
        # os.mkfifo(json_f)
    print('star load')
    # 获取网页书籍列表
    print(url_ls[folder_name])
    html_book_list = dl_request.get_html(url_ls[folder_name])
    print(html_book_list)
    data_book_list = etree.HTML(html_book_list).xpath('//h4[@class="title"]/a/@href')
    print(data_book_list)
    print('end load')
    i = 1

    # 遍历每本书的url
    for book_url in data_book_list:
        i = i + 1
        print(i)
        really_book_url = domain + book_url  # 拼串
        html_book_page = dl_request.get_html(really_book_url)  # 进入到每本书的详细页面
        data = etree.HTML(html_book_page)

        title_temp = data.xpath('//h1/text()')[0]
        title = ''
        alias = ""
        i = 0
        flg = False
        for each_char in str(title_temp):
            if '（' == each_char:
                flg = True
                break
            i = i + 1
        if flg:
            alias = str(title_temp[i:])  # 得到alias
            title = str(title_temp[0:i])  # 得到标题

        description1 = str(data.xpath('//p[@class="subtitle"]/text()')[0])

        json = {'title': title, 'alias': alias, 'description1': description1}  # 建立json串

        author = str(data.xpath('//p[@class="author"]/span/a/text()'[0]))
        detail_list = data.xpath('//div[@class="article-meta"]/p')
        for item in detail_list:
            dic_key = str(item.xpath('/p/span[1]')[0])
            dic_value_list = item.xpath('/p/span[2]//text()')
            dic_value = ''
            for each_value in dic_value_list:
                dic_value += each_value
            json[dic_key] = each_value
        score_list = data.xpath('//span[@class="score"]')
        try:
            json['自带评分'] = str(score_list[0])
            json['豆瓣读书评分'] = str(score_list[1])
        except:
            pass
        description2_list = data.xpath('//div[@class="info"]/p/text()')
        description2 = ""
        for each_des in description2_list:
            description2 += str(each_des)
        json["description2"] = description2

        comment_url = domain + str(data.xpath('//div[@class="mixed-comment-list ebook-page"]/a/@href')[0])
        comment_page = dl_request.get_html(comment_url)
        comment_content = {}
        print("Writing")
        with open(title_f, 'a+', encoding='UTF-8') as f_ti:
            f_ti.writelines(title)
        with open(description2_f, 'a+', encoding='UTF-8') as f_des:
            f_des.writelines(description2)
        print("Writed")

print("Done!")
