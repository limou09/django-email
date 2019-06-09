from django.test import TestCase
from .models import *
# Create your tests here.

# #	新闻分类添加
# news_cag = NewsCategory()
# news_cag.cag_name = "军事新闻"
# news_cag.save()

# #	新闻信息添加
# news_info = NewsInfo()
# news_info.news_title = "中国8艘核动力航母已部署到太平洋地区"
# news_info.news_content = "据新华社报道, 中国8艘核动力航母已部署到太平洋地区，随时准备和美国对抗,将美军赶出亚太地区."
# news_info.news_cag = news_cag
# news_info.save()

areas = [("北京", None),
         ("河北", None),
         ("海淀区", 1),
         ("昌平区", 1),
         ("顺义区", 1),
         ("房山区", 1),
         ("朝阳区", 1),
         ("丰台区", 1),
         ("石家庄", 2),
         ("唐山", 2),
         ("保定", 2),
         ("邢台", 2),
         ("邯郸", 2),
         ("秦皇岛", 2)]

for area in areas:
    area_info = AreaInfo()
    area_info.area_name = area[0]
    area_info.area_parent_id = area[1]
    area_info.save()