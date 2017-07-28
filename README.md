# Pynstein
Python tool for solving Einstein (zebra) puzzles using different conditions.

## Conditions
To solve the puzzle one can use the following conditions:

* **Info-Conditions**

   Info-conditions simply discribe a single column, like *"The Englishman lives in the red house"*

* **Position-Conditions**

   Position-conditions are just like Info-conditions, but they have a preset column index, e.g. *"The Norwegian lives in the first house"*

* **NextTo-Conditions**

   NextTo-conditions mean that two columns are next to each other, regardles of the order, e.g. *"The man who smokes Chesterfields lives in the house next to the man with the fox"*

* **LeftOf/RightOf-Conditions**

   LeftOf/RightOf-conditions are like NextTo-condions, but with a difinite order of the columns, e.g. *"The green house is immediately to the right/left of the ivory house"*
   
### Exclude conditions
If you want to exclude a certain condition, e.g. "A is **NOT** left of B", simply use the normal condition "A **IS** left of B" and pass the additional parameter `exclude=True`.
   
Example: `puzzle.AddCondition_LeftOf(["A"], ["B"], exclude=True)`
   
### Somewhere conditions
For `AddCondition_RightOf`and `AddCondition_LeftOf` you can pass the additional parameter `somewhere` which - if set to `True` - means that the condition will be met if A is anywhere left of/right of B, not just next to it.
   
Example: `puzzle.AddCondition_LeftOf(["A"], ["B"], somewhere=True)`

**Note: If wrap-mode is enabled, this will throw an error!**
   

## Usage

Usage is simple. Just pass the conditions, no need to specify the shape of the grid.

For example the classic puzzle taken from the 1962 *Life international magazine* that looks like the following:

```
There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
```

Would translate to:

```python
# [nationality, color, animal, drink, brand]
puzzle = Pynstein()

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

puzzle.Solve()
print(puzzle.Solutions)
```

**Note that unknown fields must be *None*. Trailing None-fields can be dropped.**

The full example can be seen under *example.py*
