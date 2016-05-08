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
from collections import OrderedDict
from Comment import Comment 
from ExcelWriter import ExcelWriter 
from Utils import date_format, delete_reply_tag

reload(sys)
sys.setdefaultencoding("utf-8")


APP_KEY = "2578051438"
APP_SECRET = "35379dbaf44658cff1c23759717e8e15"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
#1. get code
print url
print "Please copy the url into you browser, then input your account and pass and click the confirm button to get the code in the url:"
code = raw_input()
print code
# 2. access token
res = client.request_access_token(code)
access_token = res.access_token
expires_in = res.expires_in
# 3. save access token
client.set_access_token(access_token, expires_in)


def write_comment_txt(comment, fp=None):
	if not isinstance(comment, Comment):
		raise Exception("comment is not a instance of Comment")

	if fp is None:
		raise Exception("fp is not a valid file handle")
	fp.writelines(comment.vars_to_str()+'\n')


def write_comment_xls(comment, raw=0, xw = None):
	'''
	| datetime | reply_comment_user_name| reply_comment_text | comment_user_name | comment_text |
	'''
	if not isinstance(comment, Comment):
		raise Exception("comment is not a instance of Comment")
	if not isinstance(xw, ExcelWriter):
		raise Exception("xw is not a instance of ExcelWriter")

	xw.write(raw, 0, date_format(comment.reply_comment_created_time))
	xw.write(raw, 1, comment.reply_comment_user_name)
	xw.write(raw, 2, delete_reply_tag(comment.reply_comment_text))
	
	xw.write(raw, 3, date_format(comment.comment_created_time))
	xw.write(raw, 4, comment.comment_user_name)
	xw.write(raw, 5, delete_reply_tag(comment.comment_text))

def write_head(xw=None):
	xw.write(0, 0, "CommentDate")
	xw.write(0, 1, "CommentUser")
	xw.write(0, 2, "CommentText")	
	xw.write(0, 3, "ReplyDate")
	xw.write(0, 4, "ReplyUser")
	xw.write(0, 5, "ReplyText")
	

		
def request_comments():
	#request comments
	fp = open("res.txt", "a")
	xw = ExcelWriter("res.xls")
	xw.add_sheet("test")
	# write head
	write_head(xw)

	polled_num = 0
	current_page = 1
	comment_count = 1
	while(True):
		print "get %s" % current_page
		content =  client.comments.timeline.get(page=current_page)
		total_number = content.total_number
		recv_num = len(content.comments)
		if recv_num == 0:
			print "recv_num = 0"
			break
		
		for comment in content.comments:
			commentRecord = Comment()
			if(comment.has_key("reply_comment")):
				commentRecord.is_reply = True
				commentRecord.reply_comment_id = comment.reply_comment.id
				commentRecord.reply_comment_text = comment.reply_comment.text
				commentRecord.reply_comment_created_time = comment.reply_comment.created_at
				commentRecord.reply_comment_user_id = comment.reply_comment.user.id
				commentRecord.reply_comment_user_name = comment.reply_comment.user.name
			commentRecord.comment_id = comment.id
			commentRecord.comment_text = comment.text
			commentRecord.comment_created_time = comment.created_at
			commentRecord.comment_user_id = comment.user.id
			commentRecord.comment_user_name = comment.user.name

			commentRecord.weibo_id = comment.status.id
			commentRecord.weibo_text = comment.status.text
			commentRecord.weibo_user_id = comment.status.user.id
			commentRecord.weibo_user_name = comment.status.user.name

			fp.writelines(commentRecord.vars_to_str()+'\n')
			# print commentRecord.is_reply, comment_count
			if commentRecord.is_reply == True:
				write_comment_xls(commentRecord, raw=comment_count, xw=xw)
				comment_count += 1

		polled_num += recv_num
		print total_number, polled_num, current_page
		if(polled_num < total_number):
			current_page += 1
		else:
			break
	xw.save()
	fp.close()

if __name__ == "__main__":
	# request_comments()