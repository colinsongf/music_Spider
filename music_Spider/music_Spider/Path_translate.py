#!coding=utf-8

import re

#相对url转绝对url，假定将从网页中提取的不是http开头的，全部替换成从Index_Url中的第一个/前面部分+网页中提取到的部分					
#你传进来的是list，就返回list；是str，就返回str。一一对应的
def Relative_to_Absolute(index_url,url_tail):
	#把http://..../匹配出来
	head_url = re.search(r'(.+//).+?/',index_url).group()
	if type(url_tail) is list:
		res_urls = []
		if (not re.search(r'^http://',url_tail[0])) and (not re.search(r'^https://',url_tail[0])):
			#print "批量，相对转绝对.........."
			if re.search(r'^/',url_tail[0]):
			#带有/开头的url，要去除掉这个/，再拼接
				for url in url_tail:
					url = re.sub(r'^/',"",url)
					res_urls.append(head_url + url)
			else:
				for url in url_tail:
					res_urls.append(head_url + url)
			return res_urls
		else:
			return url_tail
	else:
		if (not re.search(r'^http://',url_tail)) and (not re.search(r'^https://',url_tail)):
			if re.search(r'^/',url_tail):
				return head_url + re.sub(r'^/',"",url_tail)
			else:
				return head_url + url_tail
		else:
			return url_tail

def Get_Valid_Url(urls):
	if type(urls) is list and len(urls) > 1:
		res_urls = []
		if re.search(r'^//',urls[0]):
			for url in urls:
				res_urls.append("https://"+re.sub(r'^//',"",url))
		else:
			res_urls = urls
		return res_urls
	else:
		if re.search(r'^//',''.join(urls)):
			return re.sub(r'^//',"",''.join(urls))
		else:
			return ''.join(urls)
			

def get_HeadUrl(index_url):
	return re.sub("(\d+)$","{page}",index_url)
	
	