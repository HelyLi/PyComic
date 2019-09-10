#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
# import urllib3
# from urllib3.request import urlretrieve
import requests
# regex = re.compile(r'(MyGame\:getAppConfig\(\):getImgName\(\"([#."a-zA-Z1-9_]+)\"\))')
# regex = re.compile(r'eval(.*)\$', re.DOTALL)

from lxml import etree

# import sys
# from reportlab.lib.pagesizes import portrait
# from reportlab.pdfgen import canvas
# from PIL import Image

base_url = "http://m.80images.com"

page_list = ["/list/"]

chapter_next_list = []

def main():
    # html = etree.parse("./index.html")
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)
    # second()
    list_item("/list/0_1.html")
    # book_item("/book/1547/")
    # chapter_item("/comic/44791.html", "0001")
    
def list_item(pageurl):
    # html = etree.HTML(url)
    page_list.append(pageurl)
    html = etree.parse("{0}{1}".format(base_url, pageurl), etree.HTMLParser())
    html_data = etree.tostring(html, pretty_print=True)
    res = html_data.decode('utf-8')
    # print(res)

    pic_items = html.xpath('/html/body/div/div/div/div/article/div/ul/li/a/@href')
    # print(pic_items)
    for pic_item in pic_items:
        print(pic_item)
        pic_url = pic_item.encode('utf-8').decode()
        book_item(pic_url)

    print("-------------->")
    pages = html.xpath('/html/body/div/div/div/a/@href')
    # print(pages)
    for book in pages:
        book_url = book.encode('utf-8').decode()
        include = False
        for page in page_list:
            if book_url == page:
                include = True
        if include == False:
            print(book_url)
            list_item(book_url)
        # print(book_url)
        # if book_url != pageurl :
        #     print(book_url)
        #     list_item(book_url)


def book_item(bookurl):
    regex = re.compile(r'(\d+)', re.DOTALL)
    mo = regex.search(bookurl)
    bookdir = ""
    if None != mo:
        print(mo.group(1))
        bookdir = os.path.join(os.getcwd(), mo.group(1))
        if not os.path.exists(bookdir):
            os.makedirs(bookdir)


    html = etree.parse("{0}{1}".format(base_url, bookurl), etree.HTMLParser())
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)

    chapter_list = html.xpath('/html/body/div/div/ul/li/a/@href')
    for chapter in chapter_list:
        # print(chapter)
        chapterl_url = chapter.encode('utf-8').decode()
        print(chapterl_url)
        chapter_item(chapterl_url, bookdir)

def chapter_item(chapterl_url, bookdir):
    if not os.path.exists(bookdir):
        os.makedirs(bookdir)
    chapter_next_list.append(chapterl_url)
    html = etree.parse("{0}{1}".format(base_url, chapterl_url), etree.HTMLParser())
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)

    img_list = html.xpath('/html/body/div/div/img/@src')
    for img in img_list:
        # print(chapter)
        img_url = img.encode('utf-8').decode()
        print(img_url)
        if not os.path.exists(os.path.join(bookdir, os.path.basename(img_url))):
            r = requests.get(img_url, stream=True)
            with open(os.path.join(bookdir, os.path.basename(img_url)), 'wb') as f:
                for chunk in r.iter_content(chunk_size=32):
                    f.write(chunk)
        # print(os.path.split(img_url))
        # urlretrieve(url = img_url,filename = )

    chapter_next = html.xpath('/html/body/div/div/div/a/@href')
    print(chapter_next)
    for ch_next_url in chapter_next:
        # print(chapter)
        chapter_next_url = ch_next_url.encode('utf-8').decode()
        if chapter_next_url.find("comic") > 0:
            include = False
            for t_url in chapter_next_list:
                if chapter_next_url == t_url:
                    include = True
            if include == False:
                print(chapter_next_url)
                chapter_item(chapter_next_url, bookdir)

# def second():
#     html = etree.parse('./index_35901.html', etree.HTMLParser())
#     html_data = etree.tostring(html, pretty_print=True)
#     res = html_data.decode('utf-8')

#     print(res)

#     list_data = html.xpath('/html/body/div/div/ul/li/a/@href')
#     print(list_data)
#     for i in list_data:
#         print(i)

# def four():
#     html = etree.parse('http://m.hanguomh.com/35901/01.html', etree.HTMLParser())
#     html_data = etree.tostring(html, pretty_print=True)
#     res = html_data.decode('utf-8')
#     # print(res)

#     mo = regex.search(res)
#     if None != mo:
#         # print(mo)
#         print(mo.group(1))
        # print("old.line=" + line)
        # line = auditRegex.sub("\"{}.png\"".format(mo.group(2)), line)
        # print("new.line=" + line)


if __name__ == '__main__':
    main()


    