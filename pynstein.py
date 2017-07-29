#!/usr/bin/env python3
import copy
import itertools


class Pynstein(object):

	def __init__(self):
		self._init()

	def _init(self):
		self.Set_Wrap(False)
		self._rows = None
		self._cols = None
		self._isPrepared = False
		self._items = []
		self._solutions = []
		self._conditions = {
			"info" : [],
			"position": {},
			"next_to": [],
			"left_of": [],
			"distance": []
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

	def _getPosition(self, maxRowIndex, column):
		""" Tries to find the position of a given column in the current puzzle-matrix
		Returns index >= 0 if found, -1 if only None-values were checked, else None
		"""
		firstIndex = None
		for rowIndex, item in enumerate(column):
			if rowIndex > maxRowIndex:
				break
			if item is not None:
				index = self._items[rowIndex].index(item)
				if firstIndex is not None:
					if index != firstIndex:
						return None
				else:
					firstIndex = index
		return firstIndex if firstIndex is not None else -1

	def _checkConditions(self, maxRowIndex):
		""" Checks all conditions
		Returns True, if all conditions are successfully met
		"""
		
		# position-conditions
		for position in self._conditions["position"]:
			for condition in self._conditions["position"][position]:
				# 'check XOR exclude' bust be true
				if self._checkAtPosition(maxRowIndex, condition["column"], position) == condition["exclude"]:
					return False

		# info-conditions
		for condition in self._conditions["info"]:
			if (self._getPosition(maxRowIndex, condition["column"]) is not None) == condition["exclude"]:
				return False

		# leftOf-conditions
		for condition in self._conditions["left_of"]:
			if self._checkLeftOf(maxRowIndex, condition["leftColumn"], condition["rightColumn"], condition["somewhere"]) == condition["exclude"]:
				return False

		# nextTo-conditions
		for condition in self._conditions["next_to"]:
			if self._checkNextTo(maxRowIndex, condition["column1"], condition["column2"]) == condition["exclude"]:
				return False

		# distance-conditions
		for condition in self._conditions["distance"]:
			if self._checkDistantTo(maxRowIndex, condition["firstColumn"], condition["secondColumn"], condition["distance"]) == condition["exclude"]:
				return False

		return True

	def _checkAtPosition(self, maxRowIndex, column, columnIndex):
		for rowIndex, item in enumerate(column):
			if rowIndex > maxRowIndex:
				break
			if item is not None:
				if not self._items[rowIndex][columnIndex] == item:
					return False
		return True

	def _checkLeftOf(self, maxRowIndex, leftColumn, rightColumn, somewhere, distance=1):
		leftIndex = self._getPosition(maxRowIndex, leftColumn)
		if leftIndex is not None:
			# only None-values so far
			if leftIndex == -1:
				return True
			rightIndex = self._getPosition(maxRowIndex, rightColumn)
			if rightIndex is not None:
				# only None-values so far
				if rightIndex == -1:
					return True
				if not somewhere:
					if self._wrap:
						return ((leftIndex + distance) % self._cols) == rightIndex
					else:
						return (leftIndex + distance) == rightIndex
				else:
					return leftIndex < rightIndex
		return False

	def _checkNextTo(self, maxRowIndex, column1, column2):
		return self._checkLeftOf(maxRowIndex, column1, column2, False) or self._checkLeftOf(maxRowIndex, column2, column1, False)

	def _checkDistantTo(self, firstColumn, secondColumn, distance):
		return self._checkLeftOf(maxRowIndex, firstColumn, secondColumn, False, distance) or self._checkLeftOf(maxRowIndex, secondColumn, firstColumn, False, distance)

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
		Info conditions consist of just one column
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
		NextTo conditions mean that two columns are next to each other, regardles of the order
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
		assert (not somewhere) or (not self._wrap), "Cannot set somewhere=True if wrapmode is enabled!"
		self._checkColumn(leftColumn)
		self._checkColumn(rightColumn)
		self._unprepare()
		self._conditions["left_of"].append({"leftColumn": leftColumn, "rightColumn": rightColumn, "somewhere": somewhere, "exclude": exclude})

	def AddCondition_RightOf(self, rightColumn, leftColumn, somewhere=False, exclude=False):
		""" Add a rightOf condition
		This is the same as the leftOf condition, just with swapped columns
		"""
		self.AddCondition_LeftOf(leftColumn, rightColumn, somewhere, exclude)

	def AddCondition_Distance(self, firstColumn, secondColumn, distance, exclude=False):
		""" Add a distance condition
		Distance conditions ensure that two given columns have a fixed distance to each other
		"""
		assert isinstance(distance, int), "Distance has to be int!"
		assert distance >= 1, "Distance has to be >= 1"
		self._checkColumn(firstColumn)
		self._checkColumn(secondColumn)
		self._unprepare()
		self._conditions["distance"].append({"firstColumn": firstColumn, "secondColumn": secondColumn, "distance": distance, "exclude": exclude})

	def Set_Wrap(self, wrap):
		assert isinstance(wrap, bool), "Must be boolean value!"
		if wrap:
			# check if there is a condiotion with somewhere=True
			assert len([condition for condition in self._conditions["left_of"] if condition["somewhere"]]) == 0, "Cannot set wrapmode if a condition has somewhere=True"
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
		self._cols = len(self._items[0])
		self._rows = len(self._items)
		self._isPrepared = True

	def _solve(self, rowIndex):
		
		if rowIndex >= len(self._items):
			self._solutions.append(copy.deepcopy(self._items))
			return

		# safe
		originalRow = copy.deepcopy(self._items[rowIndex])

		for rowPermutation in itertools.permutations(originalRow):
			self._items[rowIndex] = rowPermutation
			if self._checkConditions(rowIndex):
				self._solve(rowIndex + 1)

		# restore
		self._items[rowIndex] = originalRow

	def Solve(self):
		if not self._isPrepared:
			self.Prepare()
		originalItems = copy.deepcopy(self._items)
		self._solve(0)

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
	def Solutions(self):
		return self._solutions

	@property
	def Wrap(self):
		return self._wrap