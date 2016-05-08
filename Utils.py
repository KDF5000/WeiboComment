#!/usr/bin/python
# -*- coding: utf-8 -*-
from dateutil import parser
import re

def date_format(timestr):
	'''
	Mon Apr 25 16:45:00 +0800 2016
	'''
	#need to check the format of timestr firstly
	#next
	dd = parser.parse(timestr)
	str_time = dd.strftime('%Y-%m-%d %H:%M:%S')
	return str_time

def delete_reply_tag(str):
	'''
	delete reply tags in str
	e.g.: 回复@SRIOV_TCloud: hahha:  ==> hahha
	'''
	pattern = re.compile(ur"^回复@\w+:")
	match = pattern.match(str.strip())
	if match:
		end_pos = match.end()
		return str[end_pos: ]
	return str


if __name__ == "__main__":
	print date_format("Mon Apr 25 16:45:00 +0800 2016")
	comment = "回复@KDF5000:时间挤挤总是有的[鼓掌]不看电视怎么度过那段悲惨的日子"
	print delete_reply_tag(comment)
