import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
# parameter
# https://mp.weixin.qq.com/s/+article

def check_for_updates(article_array):
    #compare article names with loacl history
    #input: articles names fetched from database in a list
    #output: article name(s) that need to be updated in a list
    if not article_array or len(article_array)==0:
        return []
    elif(not os.path.exists("article.csv")):
        df = pd.DataFrame(columns = ["article"])
        df.to_csv("article.csv",index=False)

    to_be_fetch = []
    data = pd.read_csv("article.csv")

    for item in article_array:
        if(item not in data["article"].values):
            to_be_fetch.append(item)
            data.loc[len(data["article"])]=item
    if len(to_be_fetch) > 0:
        data.to_csv("article.csv",index=False)
        print("new added articles:")
        for i in to_be_fetch:
            print(i)
        print("\n")
    else:
        print("all articles are up to date")
    return to_be_fetch


def get_all_articles():
    #get all articles from database
    #input: None
    #output: all article ids in an array: article_array
    article_array = []

    try:
        connection = pymysql.connect(host="144.202.113.228",user="root",\
        password="cgsa",port=3306, db="cgsa", charset="utf8")

        cursor = connection.cursor()
        cursor.execute('SELECT post_url FROM post;')
        result = cursor.fetchall()
        for row in result:
            article_array.append(row[0].strip())
        connection.close()

    except(pymysql.err.OperationalError):
        print("Database connection failed")

    return article_array



    return article_array

def make_article_html(article):
    #generate an html page based on input, in the loacl path
    #input:id of single article
    #output:None

    header = {'accept': 'application/json, text/plain, */*',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
              'origin': 'https://mp.weixin.qq.com',
              'sec-fetch-dest':'empty',
              'sec-fetch-mode':'cors',
              'sec-fetch-site':'same-origin',
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) \
                            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 \
                            Safari/537.36'
             }
    img_header = {
        'accept': 'text/html,application/xhtml+xml,\
                  application/xml;q=0.9,image/avif,image/webp,image/apng,\
                  */*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'max-age=0',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'cross-site',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 \
                    Safari/537.36'
    }

    print('[Info] Fetching content ...')
    url = 'https://mp.weixin.qq.com/s/'+article
    website = requests.get(url, headers=header)
    soup = BeautifulSoup(website.text, 'lxml')
    output_html = soup.prettify()
    imgs = soup.findAll('img')
    img_urls = []
    for imgs in imgs:
        try:
            img_urls.append(imgs['data-src'])
        except:
            print('Blank image')

    if not os.path.isdir(article):
        os.mkdir(article)
    img_dict = {}

    print('[Info] Fetching images...')
    for i, img_url in enumerate(img_urls):
        try:
            img_format = img_url.split('=')[-1]
            img_response = requests.get(img_url,headers=img_header)
            file = open("{}/{}.{}".format(article,i,img_format), "wb")
            img_dict[img_url] = "{}/{}.{}".format(article,i,img_format)
            file.write(img_response.content)
            file.close()

            old_img = 'data-src="'+img_url+'"'
            new_img = 'src="'+img_dict[img_url]+'"'
            output_html = output_html.replace(old_img,new_img)
        except:
            print('error')

    # replace width
    for i in range(20,80,5):
        ori_width = i
        new_width = i-1
        output_html = output_html.replace('width: '+str(ori_width)+'%','width: '+str(new_width)+'%')

    print('[Info] Output file...')
    f = open(article+".html", "w", encoding='utf-8')
    f.write(output_html)
    f.close()
    print('Done\n')

def run():
    articles = get_all_articles()
    check_for_updates(articles)
    for article in articles:
        if(os.path.exists(article + ".html")):
            continue
        make_article_html(article)

if __name__ == "__main__":
    run()
