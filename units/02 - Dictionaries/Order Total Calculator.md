---
title: Order Total Calculator
---

## Overview

You are a restaurant owner. Write a program that takes a customer's order and
then outputs what they ordered and the total bill. You will need to use a
dictionary, conditionals, and loops to complete this assignment.

## Instructions

This is the menu of your restaurant:

- Falafel $4.50
- Hummus $2.25
- Shwarma $8.49
- Kebab $11.29
- Lemonade $1.75

Write a program that takes as input a selection from the menu. It should repeat
that action until the user enters \quoted{done} instead of a menu selection.
After the user enters \quoted{done}, the program should output all the items
the user ordered, and then the total bill (add all of the totals together).

As a hint, here is how you could structure the loop that takes the order until
done:

```python
while True:
    order = input("What would you like to order? ")
    if order == "done":
        break

    # Write your code that keeps track of the order here
```

## Example

\vspace{.1in}

```
What would you like to order? Shwarma
What would you like to order? Falafel
What would you like to order? Lemonade
What would you like to order? done

You ordered: Shwarma, Falafel, Lemonade.
Your bill is $14.74
```
