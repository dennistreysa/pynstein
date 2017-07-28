#!/usr/bin/env python3

class Pynstein(object):

	def __init__(self):
		self._init()

	def _init(self):
		self._rows = None
		self._cols = None
		self._constraints = {
			"info" : [],
			"position": {}
		}

	def _checkConstraint(self, constraint):
		assert isinstance(constraint, list), "Constraint has to be listtype!"
		assert len(constraint) > 0, "Could not find any data"
		assert len([c for c in constraint if c is not None]) > 0, "Could not find any non-none data!"

	def _checkPosition(self, position):
		assert isinstance(position, int), "Position has to be int!"
		assert position >= 0, "Position has to be int!"

	def AddConstraint_Info(self, constraint):
		""" Add an info constraint
		Info contraints consist of just one column
		e.g. "The Englishman lives in the red house"
		"""
		self._checkConstraint(constraint)
		self._constraints["info"].append(constraint)

	def AddConstraint_Position(self, constraint, position):
		""" Add a position constraint
		Position contraints are like info constraints, but have a fixed position
		e.g. "The Norwegian lives in the first house"
		"""
		self._checkConstraint(constraint)
		self._checkPosition(position)
		if position not in self._constraints["position"]:
			self._constraints["position"][position] = []
		self._constraints["position"][position].append(constraint)

	def Prepare(self):
		pass

	def StartOver(self):
		self._init()

	@property
	def Rows(self):
		return self._rows

	@property
	def Cols(self):
		return self._cols