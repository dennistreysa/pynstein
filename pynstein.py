#!/usr/bin/env python3

class Pynstein(object):

	def __init__(self):
		self._init()

	def _init(self):
		self._rows = None
		self._cols = None
		self._conditions = {
			"info" : [],
			"position": {},
			"next_to": [],
			"left_of": []
		}

	def _checkColumn(self, column):
		assert isinstance(column, list), "Column has to be listtype!"
		assert len(column) > 0, "Could not find any data"
		assert len([c for c in column if c is not None]) > 0, "Could not find any non-none data!"

	def _checkPosition(self, position):
		assert isinstance(position, int), "Position has to be int!"
		assert position >= 0, "Position has to be int!"

	def _getPosition(self, column):
		""" Tries to find the position of a given column in the current puzzle-matrix
		Returns index >= 0 if found, else None
		"""
		pass

	def _checkConditions(self):
		""" Checks all conditions
		Returns True, if all conditions are successfully met
		"""
		pass

	def AddCondition_Info(self, column, exclude=False):
		""" Add an info condition
		Info contraints consist of just one column
		e.g. "The Englishman lives in the red house"
		"""
		self._checkColumn(column)
		self._conditions["info"].append({"column": column, "exclude": exclude})

	def AddCondition_Position(self, column, position, exclude=False):
		""" Add a position condition
		Position conditions are like info conditions, but have a fixed position
		e.g. "The Norwegian lives in the first house"
		"""
		self._checkColumn(column)
		self._checkPosition(position)
		if position not in self._conditions["position"]:
			self._conditions["position"][position] = []
		self._conditions["position"][position].append({"column": column, "exclude": exclude})

	def AddCondition_NextTo(self, column1, column2, exclude=False):
		""" Add a nextTo condition
		NextTo conditions mean that to columns are next to each other, regardles of the order
		e.g. "The man who smokes Chesterfields lives in the house next to the man with the fox"
		"""
		self._checkColumn(column1)
		self._checkColumn(column2)
		self._conditions["next_to"].append({"column1": column1, "column2": column2})

	def AddCondition_LeftOf(self, leftColumn, rightColumn, exclude=False):
		""" Add a leftOf condition
		LeftOf conditions are like nextTo condions, but with a difinite order of the columns
		e.g. "The green house is immediately to the right/left of the ivory house"
		"""
		self._checkColumn(leftColumn)
		self._checkColumn(rightColumn)
		self._conditions["left_of"].append({"leftColumn": leftColumn, "rightColumn": rightColumn})

	def AddCondition_RightOf(self, rightColumn, leftColumn, exclude=False):
		""" Add a rightOf condition
		This is the same as the leftOf condition, just with swapped columns
		"""
		self.AddCondition_LeftOf(leftColumn, rightColumn, exclude)

	def Prepare(self):
		pass

	def Solve(self):
		pass

	def StartOver(self):
		self._init()

	@property
	def Rows(self):
		return self._rows

	@property
	def Cols(self):
		return self._cols

	@property
	def Items(self):
		return []