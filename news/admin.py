from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):

	#	显示字段
	list_display = ['id','cag_name']

@admin.register(NewsInfo)
class NewsInfoAdmin(admin.ModelAdmin):

	#	显示字段
	list_display = ['id','news_title','news_content','news_cag']
