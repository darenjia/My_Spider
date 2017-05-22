# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output/output.html', 'w', encoding='utf-8')
        fout.writelines('<html>')
        fout.writelines('<head>')
        fout.writelines("<meta charset='utf-8'>")

        fout.writelines("<link  rel='Stylesheet' href='css/base.css'/>")
        fout.writelines("<link rel='Stylesheet' href='css/style.css'/>")
        fout.writelines('</head>')
        fout.writelines('<body>')
        fout.writelines('<h1>Python爬虫爬取百度百科</h1>')
        fout.writelines("<table class='tb'>")
        fout.writelines("<tr class='td_th'><th>名称</th> <th>简介内容</th>  </tr>")
        for data in self.datas:
            fout.writelines("<tr class='td_tr'>")
            fout.writelines("<td class='td_title to'><a href='%s' target='_blank'>%s</a></td>" % (data['url'], data['title']))
            fout.writelines("<td class='td_summary to'>%s</td>" % data['summary'])
            fout.writelines('</tr>')
        fout.writelines('</table>')
        fout.writelines('</body>')
        fout.writelines('</html>')
        fout.close()
