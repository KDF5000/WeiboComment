#!/usr/bin/python
# -*- coding: utf-8 -*-

class Comment(object):

	def __init__(self):
		self.comment_id = ""
		self.comment_text = ""
		self.comment_created_time = ""

		self.comment_user_id = "" 
		self.comment_user_name = ""
		
		self.weibo_id = ""
		self.weibo_text = ""
		self.weibo_user_id = ""
		self.weibo_user_name = ""

		self.is_reply = False
		self.reply_comment_id = "" # if have
		self.reply_comment_text = ""
		self.reply_comment_created_time = ""
		self.reply_comment_user_id = ""
		self.reply_comment_user_name = ""

	'''
	assemble all the var values to a string
	'''
	def vars_to_string(self):
		res = ""
		orderDict = OrderedDict(vars(self).items(), key = lambda t : t[0])
		for name, value in orderDict.items():
			res += unicode(value) + "\t"
		return res
	'''
	assemble all the var values to a string
	'''
	def vars_to_str(self):
		res = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (unicode(self.comment_id), 
			unicode(self.comment_text),unicode(self.comment_created_time),unicode(self.comment_user_id),
			unicode(self.comment_user_name), unicode(self.weibo_id),unicode(self.weibo_text), 
			unicode(self.weibo_user_id), unicode(self.weibo_user_name), unicode(self.reply_comment_id), 
			unicode(self.reply_comment_text),unicode(self.reply_comment_created_time), unicode(self.reply_comment_user_id), unicode(self.reply_comment_user_name) )

		return res