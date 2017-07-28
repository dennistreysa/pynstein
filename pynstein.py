#!/usr/bin/env python3

class Pynstein(object):

	def __init__(self):
		self._init()

	def _init(self):
		self.Set_Wrap(False)
		self._rows = None
		self._cols = None
		self._isPrepared = False
		self._items = []
		self._conditions = {
			"info" : [],
			"position": {},
			"next_to": [],
			"left_of": []
		}

	def _unprepare(self):
		""" Reset the 'prepared'-status
		"""
		self._isPrepared = False

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

	def _extractItems(self, items):
		for rowIndex, item in enumerate(items):
			if len(self._items) < (rowIndex + 1):
				self._items.append([])
			if item is not None:
				if item not in self._items[rowIndex]:
					self._items[rowIndex].append(item)

	def _checkItems(self):
		assert len([r for r in self._items if len(r) == len(self._items[0])]) == len(self._items), "Length of rows do not match. Did you miss any conditions?"

	def AddCondition_Info(self, column, exclude=False):
		""" Add an info condition
		Info contraints consist of just one column
		e.g. "The Englishman lives in the red house"
		"""
		self._checkColumn(column)
		self._unprepare()
		self._conditions["info"].append({"column": column, "exclude": exclude})

	def AddCondition_Position(self, column, position, exclude=False):
		""" Add a position condition
		Position conditions are like info conditions, but have a fixed position
		e.g. "The Norwegian lives in the first house"
		"""
		self._checkColumn(column)
		self._checkPosition(position)
		self._unprepare()
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
		self._unprepare()
		self._conditions["next_to"].append({"column1": column1, "column2": column2, "exclude": exclude})

	def AddCondition_LeftOf(self, leftColumn, rightColumn, somewhere=False, exclude=False):
		""" Add a leftOf condition
		LeftOf conditions are like nextTo condions, but with a difinite order of the columns
		e.g. "The green house is immediately to the right/left of the ivory house"
		"""
		self._checkColumn(leftColumn)
		self._checkColumn(rightColumn)
		self._unprepare()
		self._conditions["left_of"].append({"leftColumn": leftColumn, "rightColumn": rightColumn, "somewhere": somewhere, "exclude": exclude})

	def AddCondition_RightOf(self, rightColumn, leftColumn, somewhere=False, exclude=False):
		""" Add a rightOf condition
		This is the same as the leftOf condition, just with swapped columns
		"""
		self.AddCondition_LeftOf(leftColumn, rightColumn, somewhere, exclude)

	def Set_Wrap(self, wrap):
		assert isinstance(wrap, bool), "Must be boolean value!"
		self._wrap = wrap

	def Prepare(self):
		for conditionType in self._conditions:
			if conditionType == "info":
				for condition in self._conditions["info"]:
					self._extractItems(condition["column"])
			elif conditionType == "position":
				for conditionPos in self._conditions["position"]:
					for condition in self._conditions["position"][conditionPos]:
						self._extractItems(condition["column"])
			elif conditionType == "next_to":
				for condition in self._conditions["next_to"]:
					self._extractItems(condition["column1"])
					self._extractItems(condition["column2"])
			elif conditionType == "left_of":
				for condition in self._conditions["left_of"]:
					self._extractItems(condition["leftColumn"])
					self._extractItems(condition["rightColumn"])
		self._checkItems()

	def Solve(self):
		if not self._isPrepared:
			self.Prepare()

	def Reset(self):
		""" Resets all values to default
		"""
		self._init()

	@property
	def Rows(self):
		return self._rows

	@property
	def Cols(self):
		return self._cols

	@property
	def Items(self):
		return self._items

	@property
	def Wrap(self):
		return self._wrap