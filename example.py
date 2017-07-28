#!/usr/bin/env python3

from pynstein import Pynstein

# constraints:
#There are five houses.
	#The Englishman lives in the red house.
	#The Spaniard owns the dog.
	#Coffee is drunk in the green house.
	#The Ukrainian drinks tea.
#The green house is immediately to the right of the ivory house.
	#The Old Gold smoker owns snails.
	#Kools are smoked in the yellow house.
	#Milk is drunk in the middle house.
	#The Norwegian lives in the first house.
#The man who smokes Chesterfields lives in the house next to the man with the fox.
#Kools are smoked in the house next to the house where the horse is kept.
	#The Lucky Strike smoker drinks orange juice.
	#The Japanese smokes Parliaments.
#The Norwegian lives next to the blue house.


# [nationality, color, animal, drink, brand]
puzzle = Pynstein()


# add info-constraints

#The Englishman lives in the red house.
puzzle.AddConstraint_Info(["Englishman", "red"])

#The Spaniard owns the dog.
puzzle.AddConstraint_Info(["Spaniard", None, "dog"])

#Coffee is drunk in the green house.
puzzle.AddConstraint_Info([None, "green", None, "coffee"])

#The Ukrainian drinks tea.
puzzle.AddConstraint_Info(["Ukrainian", None, None, "tea"])

#The Old Gold smoker owns snails.
puzzle.AddConstraint_Info([None, None, "snails", None, "Old Gold"])

#Kools are smoked in the yellow house.
puzzle.AddConstraint_Info([None, "yellow", None, None, "Kools"])

#The Lucky Strike smoker drinks orange juice.
puzzle.AddConstraint_Info([None, None, None, "orange juice", "Lucky Strike"])

#The Japanese smokes Parliaments.
puzzle.AddConstraint_Info(["Japanese", None, None, None, "Parliaments"])


# add position-constraints

#Milk is drunk in the middle house.
puzzle.AddConstraint_Position([None, None, None, "milk"], 2)

#The Norwegian lives in the first house.
puzzle.AddConstraint_Position(["Norwegian"], 0)