
import html_downloader
import html_outputer
import html_parser
import url_manager
from app import app


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加到新URL库中
        self.urls.add_new_url(root_url)
        # 检测是否有新的待爬取url
        while self.urls.has_new_url():
            try:
                # 获取一个新的链接
                new_url = self.urls.get_new_url()
                # 打印 序号以及链接
                print('craw： %d:%s' % (count, new_url))
                # 下载链接内容
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 添加新的url链接到 新URL库
                self.urls.add_new_urls(new_urls)
                # 输出内容到html中
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw faild!!')
        self.outputer.output_html()
    def test(self,url):
        html_cont = self.downloader.download(url)
        div = self.parser.get_first_page(html_cont)
        for app in div:
            print(app.printf())


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    # obj_spider.craw(root_url)
    # obj_spider.test("http://www.muzisoft.com/game/")
    item = app()
    html_parser.HtmlParser.get_details('http://www.muzisoft.com/soft/330819.html', item)
