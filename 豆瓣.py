import requests
import json
from lxml import etree
from usedaili import GetHtml
import os

r_get = GetHtml()

domain = "https://read.douban.com"
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Cookie': 'viewed="25767293"; bid=ObG-Ei13wjU; _vwo_uuid_v2=D4F262E9F838D5AF3B3B0006FF3560FAC|32d743603bb8da42aee367f7fcc6ee32; gr_user_id=75e0fcdf-612c-4290-b5a2-ba30b7926733; ll="108169"; __utma=30149280.386591782.1557999295.1557999295.1558427116.2; __utmc=30149280; __utmz=30149280.1558427116.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.3.386591782.1557999295; _gid=GA1.3.822382703.1558427120; _pk_id.100001.a7dd=980b6555c04c4e5f.1558427120.2.1558435020.1558427147.; _pk_ses.100001.a7dd=*; _gat=1'
}

headers_referer = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Cookie': 'viewed="25767293"; bid=ObG-Ei13wjU; _vwo_uuid_v2=D4F262E9F838D5AF3B3B0006FF3560FAC|32d743603bb8da42aee367f7fcc6ee32; gr_user_id=75e0fcdf-612c-4290-b5a2-ba30b7926733; ll="108169"; __utma=30149280.386591782.1557999295.1557999295.1558427116.2; __utmc=30149280; __utmz=30149280.1558427116.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.3.386591782.1557999295; _gid=GA1.3.822382703.1558427120; _pk_id.100001.a7dd=980b6555c04c4e5f.1558427120.2.1558435020.1558427147.; _pk_ses.100001.a7dd=*; _gat=1',
    'Referer': ''
}


def get_book_comment_data(url, start):
    arr = str(url).split('/')
    worksId = arr[2]
    data_this = {
        "query": "\n    query getWorksComment($worksId: ID!, $limit: Int) {\n      works: works(worksId: $worksId) {\n        worksType\n        \n    ... on WorksBase {\n      comments: mixedComments(limit: $limit) {\n        \n  ... on CommentBase {\n    id\n    isHidden\n    isDeleted\n    \n  ... on CommentBase {\n    works {\n      agent {\n        id\n      }\n    }\n    user {\n      id\n      avatar: picture(size: MEDIUM)\n      name\n      url\n      ... on Agent {\n        agentName\n        hasMedal\n      }\n    }\n    createTime\n    commentType\n    ... on Review {\n      url\n      badge {\n        url\n        image\n        title\n        color\n      }\n    }\n    ... on Annotation {\n      url\n    }\n  }\n\n    \n  ... on CommentBase {\n    content\n    commentType\n    ... on Discussion {\n      refDiscussion {\n        id\n        user {\n          name\n          url\n          ... on Agent {\n            agentName\n          }\n        }\n        isDeleted\n        createTime\n        content\n      }\n    }\n    ... on Review {\n      badge {\n        label\n        color\n      }\n    }\n    ... on Annotation {\n      \n  ... on Annotation {\n    originContent {\n      rawTexts\n      startOffset\n      endOffset\n      image {\n        url\n        size { width height }\n      }\n    }\n  }\n\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    isHidden\n    isDeleted\n    content\n    user {\n      id\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    works {\n      id\n      title\n      cover\n    }\n    operationInfo {\n      editor {\n        id\n        name\n      }\n      time\n    }\n    ... on Review {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Annotation {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Discussion {\n      works {\n        title\n        url\n      }\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n    }\n    user {\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    isHidden\n    isDeleted\n    operationInfo {\n      editor {\n        id\n        name\n      }\n      time\n    }\n    ... on Review {\n      reviewId\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Annotation {\n      upvoted\n      upvoteCount\n      commentCount\n    }\n  }\n  \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n    }\n    user {\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    ... on Review {\n      reviewId\n    }\n  }\n\n  \n  ... on CommentBase {\n    id\n    commentType\n    works {\n      id\n    }\n    ... on Review {\n      reviewId\n    }\n  }\n\n\n  }\n\n      }\n      commentTotal: mixedCommentCount\n    }\n  \n      }\n    }\n  ",
        "variables": {'start': start, "worksId": worksId, "limit": 300}, "operationName": "getWorksComment"}
    return r_get.post_html(url=url_json_book, dat=json.dumps(data_this), head=headers).text


def get_book_data(url):
    get_url = domain + url
    headers_referer['Referer'] = get_url
    return r_get.get_html(get_url, head=headers_referer).text


url = 'https://read.douban.com/j/kind/'
base_path = r'C:\Users\v-jiaxwa\Desktop\4'

data = {"sort": "hot", "page": 1, "kind": 100,
        "query": "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n    title\n    cover\n    url\n    isBundle\n  \n    \n    url\n    title\n  \n    \n    author {\n      name\n      url\n    }\n    origAuthor {\n      name\n      url\n    }\n    translator {\n      name\n      url\n    }\n  \n    \n    abstract\n    editorHighlight\n  \n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: true) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    isNew\n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ",
        "variables": {}}

kind_path = base_path + '\\1'
if os.path.exists(kind_path) == False:
    os.makedirs(kind_path)
title_f = os.path.join(kind_path, 'title.txt')
description2_f = os.path.join(kind_path, 'description2.txt')
comment_f = os.path.join(kind_path, 'comment.txt')
json_f = os.path.join(kind_path, 'json.txt')

for page_num in range(28, 533):
    try:
        data["page"] = page_num
        html = r_get.post_html(url=url, dat=json.dumps(data), head=headers).text
        j = json.loads(html)
        url_json_book = 'https://read.douban.com/j/graphql'
    except:
        with open(r'C:\Users\v-jiaxwa\Desktop\4\1\wrongcomment.txt', 'a+', encoding='UTF-8') as f_wrong:
            f_wrong.writelines("第" + page_num + "页出错！\n")
        print("第", page_num, "页出错！")
    for list_json in j['list']:

        html_book_page = get_book_data(list_json['url'])
        data_html_book_page = etree.HTML(html_book_page)
        try:

            title_temp = data_html_book_page.xpath('//h1/text()')

            title = ''
            alias = ""
            i = 0
            flg = False
            for each_char in str(title_temp[0]):
                if '（' == each_char:
                    flg = True
                    break
                i = i + 1
            if flg:
                alias = str(title_temp[0])[i:]  # 得到alias
                title = str(title_temp[0])[0:i]  # 得到标题
            else:
                title = str(title_temp[0])  # 得到标题

            description1 = ""
            try:
                description1 = str(data_html_book_page.xpath('//p[@class="subtitle"]/text()')[0])  # 描述1
            except:
                pass
            json_print = {'title': title, 'alias': alias, 'description1': description1}  # 建立json串
            author = str(data_html_book_page.xpath('//p[@class="author"]/span/a/text()'[0]))  # 作者
            detail_list = data_html_book_page.xpath('//div[@class="article-meta"]/p')  # 详情的列表 需要遍历
            for item in detail_list:  # 遍历详情的for循环
                dic_key = str(item.xpath('./span[1]/text()')[0])
                dic_value_list = item.xpath('./span[2]//text()')
                dic_value = ''
                for each_value in dic_value_list:
                    dic_value += str(each_value).replace('\xa0', '').replace('"', '')

                    json_print[dic_key] = dic_value  # 加入到json串中
            score_list = data_html_book_page.xpath('//span[@class="score"]/text()')  # 得到评分的list
            try:
                json_print['自带评分'] = str(score_list[0])
                json_print['豆瓣读书评分'] = str(score_list[1])
            except:
                pass
            description2_list = data_html_book_page.xpath('//div[@class="info"]/p/text()')
            description2 = ""
            for each_des in description2_list:
                description2 += str(each_des).replace('\xa0', '').replace('"', '')
            json_print["description2"] = description2
            start_comment = 1
            ls_comment = []
            try:
                data_comment_html = json.loads(get_book_comment_data(list_json['url'], start=start_comment))
                ls_comment_res = data_comment_html['data']['works']['comments']
                str_comment = ''
                for each_comment in ls_comment_res:
                    comment_current_res = str(each_comment['content'])
                    if len(comment_current_res) > 9 and len(comment_current_res) < 144:
                        ls_comment.append(comment_current_res)
                        str_comment += str(comment_current_res).replace(" ", "") + "  "
                json_print['comments'] = ls_comment
                with open(comment_f, 'a+', encoding='UTF-8') as f_com:
                    f_com.writelines(str_comment + '\n')
            except:
                with open(r'C:\Users\v-jiaxwa\Desktop\4\1\wrongcomment.txt', 'a+', encoding='UTF-8') as f_wrong:
                    f_wrong.writelines("评论网址" + str(list_json['url']) + "出错！\n")
                print("评论网址", list_json['url'], "出错！")
            print(json_print)
            with open(title_f, 'a+', encoding='UTF-8') as f_ti:
                f_ti.writelines(title + '\n')
            with open(description2_f, 'a+', encoding='UTF-8') as f_des:
                f_des.writelines(description2 + '\n')
            with open(json_f, 'a+', encoding='UTF-8') as f_json:
                f_json.writelines(str(json_print) + '\n')
            print(title, "已写入")
        except:
            with open(r'C:\Users\v-jiaxwa\Desktop\4\1\wrongcomment.txt', 'a+', encoding='UTF-8') as f_wrong:
                f_wrong.writelines("书本网址" + str(list_json['url']) + "出错！\n")
            print("书本网址", list_json['url'], "出错！")
            continue
    print("page", page_num, '爬取完成！')
print("Done!")
