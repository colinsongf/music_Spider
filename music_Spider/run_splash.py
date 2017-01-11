#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import re
#os.system("docker run -d -it -p 8050:8050 scrapinghub/splash --max-timeout 3600")

splash_image_id = ""

os.system("docker ps | grep tingyun > temp.txt")
with open('temp.txt','r') as f:
	temp = f.read()
	try:
		splash_image_id = re.search('.{12}',temp).group().replace("/","")
	except Exception,e:
		print Exception,":",e

#print "当前的splash id是 : ",splash_image_id,"\n"

if not splash_image_id:
		os.system("docker run -it -d -p 8050:8050 --name tingyun scrapinghub/splash")
		print "Splash not exists , start success ....."
else:
		os.system("docker restart %s"%splash_image_id)
		print "Splash exists , restart success ....."

temp_file = './temp.txt'

if os.path.exists(temp_file):
		os.remove(temp_file)
		print "Delete temp_file success ....."







