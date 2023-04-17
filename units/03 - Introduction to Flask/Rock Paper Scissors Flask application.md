---
title: Rock Paper Scissors Flask app
---

## Overview

In this assignment we will implement the game of Rock Paper Scissors in a web
application.

## Instructions

Your web application should let a user play the game of Rock Paper Scissors.
Just like in previous assignments, your program should accept a user's input,
randomly make a selection for its own move, then determine the winner.

The code and logic for making a random selector for the program's own move and
determining the winner will be the same as it has before, however since we're
building a web application and not a terminal application, the code/logic for
accepting the user's input will be different.

There are different ways of accepting user input in a web application, but
since we're learning about routes in Flask, we'll use those. As a hint, your
application will need three routes for each of the possible movies
(\quoted{Rock}, \quoted{Paper}, \quoted{Scissors}). When the user navigates to
one of these routes, you will know what their choice is.
