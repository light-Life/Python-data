# !/usr/bin/pythoy
# -*- coding:utf-8 -*-
# time: 2020.4.10
# item_name: 听歌词云图
# Effect: 爬取网易云所有时间听歌排行top:1-100
import requests,re
import pyecharts.options as opts
from pyecharts.charts import WordCloud


url = 'https://music.163.com/weapi/v1/play/record?csrf_token=f7816517c86683ae43100a0c558f6bef'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'cookie': '???'#记得写上自己的cookie哦
}
data = {
    'params': '3xWHWY0hb2Tm59P1Zqkny4wTNsBOHhVQXeYFkb1nWcDepVE8xjuUJg/lvAooM3Z6yaYEGyNcvHmnCLky993JOJU/WVIg/Nlec30KzJXQZ1sI99GI39Z6nk+3yNHGIEPODjREV5M5LhIlZ4J3hWLDdRKTFDE6xV5QUXua2GO+KWy20xOMOjknIKj7kPSObZNW8RuFfulWvUU9KY/lRjV3F9vwa+3U+zvOYOtAWuRg7x8=',
    'encSecKey': '759311e05d0b1ce22b49ffae66db286d56410ec62e060ca36481547ba82517c574a0ad705e62501f977aca175e3bf4273d24a716aa6f138a64a733063dc03968f34001a54149fd8c517a3f0192f90361c0165969efb8e7bd1dff21ca85114d11c1f0423b51f25ee1d9023666c768882699620e734b75f5db36c3eb550cbacd9b'
}
def post():
    response = requests.post(url,headers=headers,data=data)
    if response.status_code == 200:
        return response.text
    return

def analysis():
    whole_time = re.findall('.*?allData":(.*?)}],"weekData".*?',post(),re.S)
    whole_time_str = str(whole_time)
    contents = re.findall('.*?"playCount":(.*?),.*?{"name":"(.*?)".*?',whole_time_str,re.S)
    return contents
#我都被这个操作惊呆了
def wordCloud(contents):
    total = []
    for content in contents:
        number = content[0]
        name = content[1]
        reversal = contents[0] = name,number
        total.append(reversal)

    (
        WordCloud()
            .add(series_name="听歌词云图", data_pair=total, word_size_range=None)
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="听歌词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=25)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render("听歌词云图.html")
    )

wordCloud(analysis())
print('\n\n\t\t云词制作完成')
