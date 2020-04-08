# !/usr/bin/pythoy
# -*- coding:utf-8 -*-
# time: 2020.3.19
import requests,re
import pyecharts.options as opts
from bs4 import BeautifulSoup
from pyecharts.charts import Line

headers = {'User-Agent':'Mozilla/5.0'}
url = 'https://www.liaoxuefeng.com/wiki/1016959663602400'
response = requests.get(url,headers=headers)

inde = re.findall('<li.*?id="off-(.*?)".*?<a.*?href="(.*?)">(.*?)</a>',response.text,re.S)
name = []
Read = []
for indes in inde:
    id = str(indes[1])
    name.append(indes[2])
    print('正在分析:',indes[2])
    urlid = 'https://www.liaoxuefeng.com'+id
    response = requests.get(urlid,headers=headers)
    if response.status_code == 200:
        inde = re.findall('<span>Reads:(.*?)</span>',response.text)
        for indes in inde:
            Read.append(indes)

#建立可视化分析图
(
    Line(init_opts=opts.InitOpts(width="1920px", height="900px"))
    .add_xaxis(xaxis_data=name)
    .add_yaxis(
        series_name="热力值",#坐标轴指示器的文本标签
        y_axis=Read,
        is_smooth=True,#是否平滑曲线
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),#填充颜色深度,默认颜色
        label_opts=opts.LabelOpts(is_show=False),#标签配置项,显示标签数字
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Python在线学习热力值",# 主标题文本，支持使用 \n 换行
            subtitle="数据来自廖雪峰Python教程", # 副标题文本，支持使用 \n 换行。
            pos_left="center",#位置自动对齐（左侧）
            pos_top="top",#位置自动对齐（上侧）
        ),
        tooltip_opts = opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),# 提示框组件
        legend_opts = opts.LegendOpts(pos_left="left"),#坐标轴指示器位置（左）
        datazoom_opts = [#显示组件
            opts.DataZoomOpts(range_start=0, range_end=100),# 数据窗口范围的起始百分比。# 数据窗口范围的结束百分比
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),#组件类型，长数据建议选用inside。同上
        ],
        xaxis_opts = opts.AxisOpts(type_="category", boundary_gap=False),# 'category': 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
        yaxis_opts = opts.AxisOpts(name="热度", type_="value", max_=850000000),# 'value': 数值轴，适用于连续数据。
    )
    .render("python.html")#路径
)
print('\n\t分析完成！')
