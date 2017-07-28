#!/usr/bin/env python3

from pynstein import Pynstein

# conditions:
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


# add info-conditions

#The Englishman lives in the red house.
puzzle.AddCondition_Info(["Englishman", "red"])

#The Spaniard owns the dog.
puzzle.AddCondition_Info(["Spaniard", None, "dog"])

#Coffee is drunk in the green house.
puzzle.AddCondition_Info([None, "green", None, "coffee"])

#The Ukrainian drinks tea.
puzzle.AddCondition_Info(["Ukrainian", None, None, "tea"])

#The Old Gold smoker owns snails.
puzzle.AddCondition_Info([None, None, "snails", None, "Old Gold"])

#Kools are smoked in the yellow house.
puzzle.AddCondition_Info([None, "yellow", None, None, "Kools"])

#The Lucky Strike smoker drinks orange juice.
puzzle.AddCondition_Info([None, None, None, "orange juice", "Lucky Strike"])

#The Japanese smokes Parliaments.
puzzle.AddCondition_Info(["Japanese", None, None, None, "Parliaments"])


# add position-conditions

#Milk is drunk in the middle house.
puzzle.AddCondition_Position([None, None, None, "milk"], 2)

#The Norwegian lives in the first house.
puzzle.AddCondition_Position(["Norwegian"], 0)


# add nextTo conditions

#The man who smokes Chesterfields lives in the house next to the man with the fox.
puzzle.AddCondition_NextTo([None, None, None, None, "Chesterfields"], [None, None, "fox"])

#Kools are smoked in the house next to the house where the horse is kept.
puzzle.AddCondition_NextTo([None, None, None, None, "Kools"], [None, None, "horse"])

#The Norwegian lives next to the blue house.
puzzle.AddCondition_NextTo(["Norwegian"], [None, "blue"])


# add rightOf conditions

#The green house is immediately to the right of the ivory house.
puzzle.AddCondition_RightOf([None, "green"], [None, "ivory"])


# add missing informations
puzzle.AddCondition_Info([None, None, None, "water"])
puzzle.AddCondition_Info([None, None, "zebra"])


# prepare (explicit)
puzzle.Prepare()