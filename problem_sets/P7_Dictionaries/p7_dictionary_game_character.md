# P7 Dictionaries Game Character


## Overview
In this assignment, you will create and work with **multiple game characters** using dictionaries. 
You will also write functions to update and display character information, and simulate a simple attack between characters.

---

## Learning Goals
- Create and use dictionaries  
- Store multiple objects (characters)  
- Update dictionary values safely  
- Write and use functions  
- Accept user input to modify a dictionary  

---

# Part 1: Create Characters

Create **three** character dictionaries.

## Requirements for each character:
- Must include:
  - `"name"` (string)
  - `"health"` (integer)

---

## Starting Character (Provided)

```python
Norm = {
    "name": "Norm the Forester",
    "health": 100
}
````

---

## Your Task

1. Create **two additional characters** of your choice
2. Add **at least two additional attributes** to `Norm`

Examples of additional attributes:

* `"weapon"`
* `"gold"`
* `"armor"`
* `"level"`
* `"attack"` ← (recommended for later use)

---

# Part 2: Update Health (Function)

Create a function:

```python
def update_health(character, amount):
```

## Requirements:

* Add `amount` to the character’s health
* Ensure:

  * health does **not go below 0**
  * health does **not go above 100**

---

# Part 3: Display Character (Function)

Create a function:

```python
def display_character(character):
```

## Requirements:

1. Display the character’s `"name"`
2. Display the character’s `"health"`
3. Display all **remaining attributes**

Use a loop to display additional attributes.

---

# Part 4: Add Attribute (User Input)

Prompt the user to enter:

* an **attribute name**
* a **value**

Add this new attribute to one of your characters (for example, `Norm`).

---

## Example Interaction

```text
Enter attribute name: mana
Enter value: 50
```

---

# Part 5: Attack Function

Create a function:

```python
def attack(attacker, defender):
```

## Requirements:

* Use the attacker's `"attack"` value
* Decrease the defender’s health
* Call `update_health()` to apply the change
* Display a message describing the attack

---

## Example Output

```text
Norm the Forester attacks Lara the Swift!
Lara the Swift loses 15 health.
```

---

# Part 6: Test Your Program

* Call `update_health()` on at least one character
* Add a new attribute using user input
* Call `attack()` once between two characters
* Call `display_character()` for all three characters

---

# Sample Output

```text
Enter attribute name: mana
Enter value: 50

Norm the Forester attacks Lara the Swift!
Lara the Swift loses 15 health.

Name: Norm the Forester
Health: 90
attack: 15
mana: 50

Name: Lara the Swift
Health: 75
attack: 12

Name: Drax the Mighty
Health: 100
armor: Heavy
```

---

# Starter Code

```python
# Starting character
Norm = {
    "name": "Norm the Forester",
    "health": 100
}

# TODO: Add at least two more attributes to Norm
# (include "attack" for battle)

# TODO: Create two additional characters


def update_health(character, amount):
    # TODO: update health
    # ensure it stays between 0 and 100
    pass


def display_character(character):
    # TODO: print name
    # TODO: print health
    # TODO: print other attributes
    pass


def attack(attacker, defender):
    # TODO:
    # get attack value
    # reduce defender health using update_health
    # print attack message
    pass


# --- User Input for New Attribute ---
# TODO: ask user for attribute name
# TODO: ask user for value
# TODO: add to Norm dictionary


# --- Test your functions ---

update_health(Norm, -20)

# TODO: call attack between two characters

display_character(Norm)

# TODO: display your other two characters
```

---

# Requirements Checklist

* Three characters created
* Each character has `"name"` and `"health"`
* Norm includes at least **two additional attributes**
* `update_health()` correctly limits values between 0 and 100
* `display_character()` prints all required information
* User input is used to add a new attribute
* `attack()` function is implemented and used

---

# Optional Challenges

* Add `"armor"` to reduce damage
* Prevent missing `"attack"` values from causing errors
* Let both characters attack each other
* Add random damage using `random.randint()`

-- end --
