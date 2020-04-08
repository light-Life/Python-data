＃！/ usr / bin / pythoy
＃-*-编码：utf-8-*-
＃时间：2020.3.19
进口 的请求，重新
进口 pyecharts。选项 为 OPTS
从 bs4  导入 BeautifulSoup
来自 pyecharts。图表 导入 线

标头 = { 'User-Agent'：'Mozilla / 5.0' }
url  =  'https://www.liaoxuefeng.com/wiki/1016959663602400'
响应 =  请求。get（url，headers = headers）

inde  =  re。findall（'<li。*？id =“ off-（。*？）”。*？<a。*？href =“（。*？）”>（。*？）</a>'，响应。文本，重新。小号）
名称 = []
阅读 = []
对于 东印度 在 不知疲倦：
    id  =  str（indes [ 1 ]）
    名字。追加（indes [ 2 ]）
    print（'正在分析：'，indes [ 2 ]）
    URLID  =  'https://www.liaoxuefeng.com' + ID
    响应 =  请求。get（urlid，headers = headers）
    如果 回应。status_code  ==  200：
        inde  =  re。的findall（'<跨度>读取：（*）</跨度>？'，响应。文本）
        对于 东印度 在 不知疲倦：
            阅读。追加（indes）

＃建立可视化分析图
（
    线（init_opts = OPTS。InitOpts（宽度= “1920px” ，高度= “900px” ））
    。add_xaxis（xaxis_data = name）
    。add_yaxis（
        series_name = “热力值”，＃坐标轴指针的文本标签
        y_axis = 读取，
        areastyle_opts = opts。AreaStyleOpts（opacity = 0.5），＃填充颜色深度，替换颜色
        label_opts = opts。LabelOpts（is_show = False），＃标签配置项，显示标签数字
    ）
    。set_global_opts（
        title_opts = 选择。TitleOpts（
            title = “ Python在线学习热力值”，＃主标题文本，支持使用\ n换行
            subtitle = “数据来自廖雪峰Python教程”，＃副标题文本，支持使用\ n换行。
            pos_left = “ center”，＃位置自动对齐（垂直）
            pos_top = “ top”，＃位置自动对齐（上侧）
        ），
        tooltip_opts  =  opts。TooltipOpts（trigger = “ axis”，axis_pointer_type = “ cross”），＃提示框组件
        legend_opts  =  opts。LegendOpts（pos_left = “ left”），＃坐标轴指示器位置（左）
        datazoom_opts  = [ ＃显示组件
            选择。DataZoomOpts（range_start = 0，range_end = 100），＃数据窗口范围的起始百分比。
            选择。DataZoomOpts（type_ = “内部”，RANGE_START = 0，RANGE_END = 100）， ＃组件类型，长数据建议选用内部。同上
        ]，
        xaxis_opts  =  opts。AxisOpts（type_ = “类别”，boundary_gap = 假）， ＃'类别'：类目轴，适用于离散的类目数据，为该类型时必须通过数据设置类目数据。
        yaxis_opts  =  opts。AxisOpts（名称= “热度”，type_ = “值”，MAX_ = 8.5亿）， ＃'值'：数值轴，适用于连续数据。
    ）
    。render（“ python.html”）＃路径
）
打印（' \ n \ t分析完成！'）
