---
title: Rock Paper Scissors, part 1
---

## Overview

In this assignment we will implement the game of Rock Paper Scissors. In order
to complete this assignment, you will need to accept user input, use comparison
operators, and conditionals as well.

## Instructions

Create a program that lets you play Rock Paper Scissors against your computer.
Your program should first randomly choose between rock, paper, or scissors.
This will be the computer's choice. It should then ask the user for their
choice with a message of \quoted{Please enter your move:}.

Next determine the winner based on the rules of Rock Paper Scissors where rock
beats scissors, scissors beats paper, and paper beats rock. If the player wins,
print \quoted{The computer chose <computers choice>, you win!} If the player
looses, print \quoted{The computer chose <computers choice>, better luck next
time.} Otherwise if it's a tie, print \quoted{The computer chose <computers
choice>, it's a tie.} \lookhere{Your text output should match this.}

## Example

\vspace{.1in}

```
Please enter your move: rock
The computer chose scissors, you win!
```

\vspace{.1in}

```
Please enter your move: scissors
The computer chose rock, better luck next time.
```

\vspace{.1in}

```
Please enter your move: paper
The computer chose paper, it's a tie.
```
