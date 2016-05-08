#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlwt

class ExcelWriter(object):
	'''
	A writer for python to write info into excel
	'''

	def __init__(self, file_name):
		if file_name is None:
			raise Exception("Illegal filename!")
		self._filename = file_name
		self._table = xlwt.Workbook()
		self._cur_sheet = None

	def save(self):
		'''
		save a excel file
		'''
		if self._table is None:
			raise Exception("No availible table!")
		self._table.save(self._filename)

	def select_sheet(self, sheet_index_or_name):
		'''
		select sheet
		@param sheet_index_or_name int | string
		'''
		if isinstance(sheet_index_or_name, int):
			try:
				self._cur_sheet = self._table.sheet_by_index(sheet_index_or_name)
			except Exception, e:
				raise Exception("The sheet doesn`t exist!")
		elif isinstance(sheet_index_or_name, string):
			try:
				self._cur_sheet = self._table.sheet_by_name(sheet_index_or_name)
			except Exception, e:
				raise Exception("The sheet doesn`t exist!")
		else:
			raise Exception("Invalid Sheet Name!")

	def add_sheet(self, sheet_name):
		'''
		add a new sheet, then the current sheet will be the new sheet
		'''
		if sheet_name is None:
			raise Exception("Invalid sheet name!")

		if self._table is None:
			raise Exception("No availible table!")
		self._cur_sheet = self._table.add_sheet(sheet_name)


	def write(self, raw, column, value):
		if self._cur_sheet is None:
			raise Exception("Please select a sheet before write!")
		try:
			self._cur_sheet.write(raw, column, value)
		except Exception, e:
			raise

	def set_cell_style(self):
		pass


if __name__ == "__main__":
	writer = ExcelWriter("demo.xls")
	writer.add_sheet("test")
	writer.write(0, 0, "demo")
	writer.save()


