
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.mail import send_mail

from .models import CityInfo

# Create your views here.

#	父级地区展示
def index(request):

	#	获取父级地区信息
	citys = CityInfo.objects.filter(area_parent=None)

	return render(request, 'index.html', locals())


#	子地区展示
def get_areas(request):
	
	#	获取地区编码
	area_code = request.GET.get('code',None)
	#	获取子地区列表
	citys = CityInfo.objects.filter(area_parent=area_code)

	#	组装数据
	city_list = []
	for city in citys:
		info = {}
		info['name'] = city.area_name
		info['code'] = city.area_code

		city_list.append(info)

	return JsonResponse({"res":city_list})


#	验证码
def email(request):
	"""
	# subject 主题
	# message 邮件文本内容
	# from_email 发送者
	# recipient_list 收件人列表
	# auth_user 邮箱服务器认证用户
	# auth_password 认证密码
	# html_message html邮件内容
	def send_mail(subject, message, from_email, recipient_list,
	          fail_silently=False, auth_user=None, auth_password=None,
	          connection=None, html_message=None):
	"""

	content = '<a href="http://localhost:8000/email/">请点击激活邮件!</a>'
	msg = '邮件测试'

	send_mail(subject='注册激活邮件',
	          from_email='limou09@163.com',
	          recipient_list=['1457753144@qq.com'],
	          html_message=content,
	          message=msg)

	return render(request, 'index.html')


