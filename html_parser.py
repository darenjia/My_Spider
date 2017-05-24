# coding:utf8
import re
import urllib.parse

from bs4 import BeautifulSoup

import html_downloader
from app import app


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取出来链接放入新URL库
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/soft/"))
        for link in links:
            new_url = link['href']
            new_url += "http://www.muzisoft.com"
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    # 获取新的内容
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    # 获取推荐
    def get_first_page(self, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        lis = list()
        apps = list()
        box_node = soup.find('div', id="appbox")
        title = box_node.find_all('b')
        app_type = box_node.find_all('ul')
        print(len(app_type))
        for i in range(0, len(app_type)):
            li = app_type[i].find_all('li')
            print(len(li))
            soft = li[0].find_all('a')
            img = li[0].find_all('img')
            for y in range(0, len(soft)):
                item = app()
                item.src = soft[y]['href']
                item.name = soft[y].get_text()
                item.imgsrc = img[y]['src']
                item.apptype = title[i].get_text()
                apps.append(item)
        return apps

    # 获取应用详情信息
    @staticmethod
    def get_details(url, app):
        html_content = html_downloader.HtmlDownloader().download(url)
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        appabout = soup.find('div', class_='appabout')
        lables = appabout.find('em').find_all('a')
        for i in lables:
            app.lable.append(i.get_text())
        ppp = appabout.find_all('p')
        for i in range(0, len(ppp)):
            if i == 0 or i == 1:
                continue
            else:
                text = ppp[i].find('em').get_text()
                if text == "大小：":
                    app.size = text
                elif text == '类别：':
                    app.apptype = text
                elif text == '版本：':
                    app.version = text
                elif text == '浏览次数：':
                    app.hot = int(text)
                elif text == '页面最后更新时间：':
                    app.lastupdatetime = text
        appinfo = soup.find('div', class_='appinfo')
        description = appinfo.find('div', id='desc').get_text()
        lis = description.split('\n')
        print(len(lis))



