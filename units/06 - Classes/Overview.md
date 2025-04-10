# Overview

In this unit we will learn about classes in Python. We’ll cover their basic
functionality, the concept of encapsulation and when and why it’s useful, and
also talk about how we’ve already been using classes (Flash,
int/string/float/etc.)

## Agenda

- Review functions and data types (focus on dict)
- How do we represent something like a dog or a student in code?
- Introduce classes
    - Grouping related data and functions together
    - Reusable
- Syntax
    - `class`
    - `__init__` method
    - `self`
    - Attributes
    - Instance variables
    - Instance methods vs functions
- Working with classes
    - Classes vs instances, blueprint -> object (e.g. blueprint for a house vs. actual house)
    - Multiple objects of the same class
    - Each has its own data


## Exercises

### Create a Student class

- Attributes: `name`, `age`, and `grade`
- Methods:
    - `introduce()` to print all of student's information
- Create multiple students and call introduce on all of them
- Put students in a list, loop over the list, and call introduce on all of them

### BankAccount Class

- Attributes: `owner`, `balance`
- Methods:
    - `deposit(amount)`
    - `withdraw(amount)`
    - `display_balance()`

### GameCharacter Class

- Attributes: `name`, `health`, and `power`
- Methods:
    - `attack(target)`
    - `is_alive()`
- Have two characters fight each other until one wins

### Flashcard Class

- Attributes: `question`, `answer`
- Methods:
    - `quiz()`, asks the question and checks if user input matches the answer
