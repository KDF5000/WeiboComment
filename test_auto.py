#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
need to install python package for weibo api
install: (http://github.liaoxuefeng.com/sinaweibopy/)
	pip install sinaweibopy
'''
from weibo import APIClient
import urllib2
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


APP_KEY = "2578051438"
APP_SECRET = "35379dbaf44658cff1c23759717e8e15"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url