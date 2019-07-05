# -*- coding: utf-8 -*-
"""
API 的使用
@author: xiaozuo
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
# http://api.github.com/ 将请求发送到github网站中响应调用API调用的部分
# search/repositories 让API搜索GitHub上的所有仓库
# 问号表示要传递一个实参, q表示查询 =让我们能够开始指定查询(q=)
# language:python 只想要关于python的仓库信息
# &sort=stars 项目按其获得的星级进行排序
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)


# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'], # star数
        'label': str(repo_dict['description']),   # 描述
        'xlink': repo_dict['html_url'],    # 链接
    }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()   # 创建了一个Pygal类Config的实例,命名为my_cpnfig 通过修改my_config的属性, 定制图形外观
my_config.x_label_rotation = 45 # X旋转45度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  # 名字字符限制为15
my_config.show_y_guides = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义宽度， 让图表充分利用浏览器的可用空间


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

