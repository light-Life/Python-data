# !/usr/bin/python
# -*- coding:utf-8 -*-
# time: 2020.3.19
import requests,re
import pyecharts.options as opts
from bs4 import BeautifulSoup
from pyecharts.charts import Line
from pyecharts.faker import Faker

headers = {'User-Agent':'Mozilla/5.0'}
url = 'https://www.liaoxuefeng.com/wiki/1016959663602400'
response = requests.get(url,headers=headers)

inde = re.findall('<li.*?id="off-(.*?)".*?<a.*?>(.*?)</a>',response.text,re.S)
name = []
Read = []
for indes in inde:
    print(indes)
    id = str(indes[0])
    name.append(indes[1])
    urlid = 'https://www.liaoxuefeng.com/wiki/1016959663602400/'+id
    response = requests.get(urlid,headers=headers)
    if response.status_code == 200:
        inde = re.findall('<span>Reads:(.*?)</span>',response.text)
        for indes in inde:
            Read.append(indes)
(
    Line(init_opts=opts.InitOpts(width="1920px", height="900px"))
    .add_xaxis(xaxis_data=name)
    .add_yaxis(
        series_name="热力值:",
        y_axis=Read,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        linestyle_opts=opts.LineStyleOpts(),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Python在线学习热力值",
            subtitle="数据来自廖雪峰Python教程",
            pos_left="center",
            pos_top="top",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100),
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
        ],
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="热度", type_="value", max_=850000000),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
        ),
        axisline_opts=opts.AxisLineOpts(),
    )
    .render("python.html")#路径
)
print('\n\t分析完成！')
