from django.db import models

# Create your models here.

#	新闻
class NewsCategory(models.Model):
	cag_name = models.CharField(max_length=30)

	def __str__(self):
		return self.cag_name

	class Meta:
		db_table = 'newscategory'
		verbose_name = '新闻分类'
		verbose_name_plural = verbose_name

class NewsInfo(models.Model):
	news_title = models.CharField(max_length=50)
	news_content = models.TextField()
	news_cag = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.news_title

	class Meta:
		db_table = 'newsinfo'
		verbose_name = '新闻信息'
		verbose_name_plural = verbose_name

#	自关联
#	地区
class AreaInfo(models.Model):
	area_name = models.CharField(max_length=50)
	#	父级地区，自关联
	area_parent = models.ForeignKey('self', null=True, blank=True, on_delete=True)

	def __str__(self):
		return self.area_name

	class Meta:
		db_table = 'areainfo'
		verbose_name = '地区信息'
		verbose_name_plural = verbose_name


class CityInfo(models.Model):
	area_code = models.CharField(max_length=20)
	area_name = models.CharField(max_length=50)
	area_parent = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.area_name

	class Meta:
		db_table = 'cityinfo'
		verbose_name = '城区信息'
		verbose_name_plural = verbose_name

# #	图书
# class BookInfo(models.Model):
# 	book_title = models.CharField(max_length=50)
# 	book_comment = models.IntegerField(default=0)
# 	book_read = models.IntegerField(default=0)
# 	book_delete = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.book_title

# 	class Meta:
# 		db_table = 'bookinfo'
# 		verbose_name = '图书信息'
# 		verbose_name_pulral = verbose_name

# class HeroInfo(models.Model):
# 	hero_name = models.CharField(max_length=50)
# 	hero_sex = models.BooleanField(default=True)
# 	hero_desc = models.TextField()
# 	hero_delete = models.BooleanField(default=False)
# 	hero_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.hero_name

# 	class Meta:
# 		db_table = 'heroinfo'
# 		verbose_name = '英雄信息'
# 		verbose_name_pulral = verbose_name