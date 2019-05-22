import requests
import json
from lxml import etree

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


def get_book_comment_data(url):
    arr = str(url).split('/')
    worksId = arr[2]
    print(worksId)
    data_this = {
        "query": "\n    query getWorksComment($worksId: ID!, $limit: Int) {\n      works: works(worksId: $worksId) {\n        worksType\n        \n    ... on WorksBase {\n      comments: mixedComments(limit: $limit) {\n        \n  ... on CommentBase {\n    id\n    isHidden\n    isDeleted\n    \n  ... on CommentBase {\n    works {\n      agent {\n        id\n      }\n    }\n    user {\n      id\n      avatar: picture(size: MEDIUM)\n      name\n      url\n      ... on Agent {\n        agentName\n        hasMedal\n      }\n    }\n    createTime\n    commentType\n    ... on Review {\n      url\n      badge {\n        url\n        image\n        title\n        color\n      }\n    }\n    ... on Annotation {\n      url\n    }\n  }\n\n    \n  ... on CommentBase {\n    content\n    commentType\n    ... on Discussion {\n      refDiscussion {\n        id\n        user {\n          name\n          url\n          ... on Agent {\n            agentName\n          }\n        }\n        isDeleted\n        createTime\n        content\n      }\n    }\n    ... on Review {\n      badge {\n        label\n        color\n      }\n    }\n    ... on Annotation {\n      \n  ... on Annotation {\n    originContent {\n      rawTexts\n      startOffset\n      endOffset\n      image {\n        url\n        size { width height }\n      }\n    }\n  }\n\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    isHidden\n    isDeleted\n    content\n    user {\n      id\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    works {\n      id\n      title\n      cover\n    }\n    operationInfo {\n      editor {\n        id\n        name\n      }\n      time\n    }\n    ... on Review {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Annotation {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Discussion {\n      works {\n        title\n        url\n      }\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n    }\n    user {\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    isHidden\n    isDeleted\n    operationInfo {\n      editor {\n        id\n        name\n      }\n      time\n    }\n    ... on Review {\n      reviewId\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Annotation {\n      upvoted\n      upvoteCount\n      commentCount\n    }\n  }\n  \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n    }\n    user {\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n    ... on Review {\n      reviewId\n    }\n  }\n\n  \n  ... on CommentBase {\n    id\n    commentType\n    works {\n      id\n    }\n    ... on Review {\n      reviewId\n    }\n  }\n\n\n  }\n\n      }\n      commentTotal: mixedCommentCount\n    }\n  \n      }\n    }\n  ",
        "variables": {"worksId": worksId, "limit": 6}, "operationName": "getWorksComment"}
    return requests.post(url=url_json_book, data=json.dumps(data_this), headers=headers).text


def get_book_data(url):
    # https://read.douban.com/ebook/34157247/
    get_url = domain + url
    headers_referer['Referer'] = get_url
    get_url = domain + url + 'subject_reviews'
    return requests.get(get_url, headers=headers_referer).text


url = 'https://read.douban.com/j/kind/'

data = {"sort": "hot", "page": 1, "kind": 100,
        "query": "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n    title\n    cover\n    url\n    isBundle\n  \n    \n    url\n    title\n  \n    \n    author {\n      name\n      url\n    }\n    origAuthor {\n      name\n      url\n    }\n    translator {\n      name\n      url\n    }\n  \n    \n    abstract\n    editorHighlight\n  \n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: true) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    isNew\n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ",
        "variables": {}}
html = requests.post(url=url, data=json.dumps(data), headers=headers).text
# print(html)
j = json.loads(html)

# print(j['list'])

url_json_book = 'https://read.douban.com/j/graphql'
for list in j['list']:
    # print(type(list))
    # print(url)
    # print(list)
    # print(get_book_comment_data(list['url']))

    html_book_page = get_book_data(list['url'])
    print(html_book_page)
    # for ll in list:
    #     print(get_book_data(list[url]))
    data = etree.HTML(html_book_page)
    print(data)
    title_temp = data.xpath('//h1')#('//h1/text()')
    print(title_temp)
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

    description1 = str(data.xpath('//p[@class="subtitle"]/text()'))

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
    print(json)
    # comment_url = domain + str(data.xpath('//div[@class="mixed-comment-list ebook-page"]/a/@href')[0])
    # comment_page = requests.get_html(comment_url)
    # comment_content = {}
    # print("Writing")
    # with open(title_f, 'a+', encoding='UTF-8') as f_ti:
    #     f_ti.writelines(title)
    # with open(description2_f, 'a+', encoding='UTF-8') as f_des:
    #     f_des.writelines(description2)
    # print("Writed")

    break
