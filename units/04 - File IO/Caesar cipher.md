---
title: Caesar cipher (part 1)
---

\graphicspath{ {"./units/04 - File IO/"/} }

## Overview

In this assignment, we will be creating a Flask application that
allows users to encode and decode messages wth a Caesar cipher. A
Caesar cipher is a simple form of encoding which \quoted{shifts} the
letters in a message by a predetermined number of spaces (for example,
minus 3 spaces) up or down the alphabet. Users are able to return the
message back to its original form by shifting the letters the same
number of spaces in the opposite direction (for example, plus 3 spaces).

For example, the letter \quoted{m} becomes \quoted{j} when shifted
minus 3 spaces. When we look at the alphabet this shift becomes a
little easier to understand:

\vspace{0.1in}
\begin{center}
\textit{a b c d e f g h i \framebox{\strut{j}} k l
\framebox{\strut{m}} n o p q r s t u v w x y z}
\end{center}
\vspace{0.1in}

Let's apply this to a longer message: \quoted{The quick fox}. We'll
continue to shift the message by minus 3 spaces, although we can
choose to shift by different number of spaces. Shifted by minus 3
spaces, we get the following letters:

\begin{align}
\quoted{T}\ -\ 3\ & \Rightarrow\ \quoted{Q} & \quoted{h}\ -\ 3\ & \Rightarrow\ \quoted{e} & \quoted{e}\ -\ 3\ & \Rightarrow\ \quoted{b} \nonumber \\
\quoted{q}\ -\ 3\ & \Rightarrow\ \quoted{n} & \quoted{u}\ -\ 3\ & \Rightarrow\ \quoted{r} & \quoted{i}\ -\ 3\ & \Rightarrow\ \quoted{f} \nonumber \\
\quoted{c}\ -\ 3\ & \Rightarrow\ \quoted{z} & \quoted{k}\ -\ 3\ & \Rightarrow\ \quoted{h} & \quoted{f}\ -\ 3\ & \Rightarrow\ \quoted{c} \nonumber \\
\quoted{o}\ -\ 3\ & \Rightarrow\ \quoted{l} & \quoted{x}\ -\ 3\ & \Rightarrow\ \quoted{u} \nonumber
\end{align}

Once encoded, our original message of \quoted{The quick fox} becomes
\quoted{Qeb nrfzh clu}. Since we shifted the message by minus 3 spaces
to encode it, we'll need to shift it by positive 3 spaces to decode
it:

\begin{align}
\quoted{Q}\ +\ 3\ & \Rightarrow\ \quoted{T} & \quoted{e}\ +\ 3\ & \Rightarrow\ \quoted{h} & \quoted{b}\ +\ 3\ & \Rightarrow\ \quoted{e} \nonumber \\
\quoted{n}\ +\ 3\ & \Rightarrow\ \quoted{q} & \quoted{r}\ +\ 3\ & \Rightarrow\ \quoted{u} & \quoted{f}\ +\ 3\ & \Rightarrow\ \quoted{i} \nonumber \\
\quoted{z}\ +\ 3\ & \Rightarrow\ \quoted{c} & \quoted{h}\ +\ 3\ & \Rightarrow\ \quoted{k} & \quoted{c}\ +\ 3\ & \Rightarrow\ \quoted{f} \nonumber \\
\quoted{l}\ +\ 3\ & \Rightarrow\ \quoted{o} & \quoted{u}\ +\ 3\ & \Rightarrow\ \quoted{x} \nonumber
\end{align}

It's important to note that the case of a letter (uppercase, or
lowercase) should be respected, meaning that uppercase \quoted{T}
becomes uppercase \quoted{Q}, and lowercase \quoted{t} becomes
lowercase \quoted{q}. Caesar cipher only alters letters; numbers and
other characters are not changed. For example, if our original message
is \quoted{The \#1 fox}, the encoded message would be \quoted{Qeb \#1
clu}.

The \quoted{shifting} of the letters can be done by taking a letter's
ASCII code (which is a number) and either adding or subtracting the
number of spaces we want to shift by. Let's look at the ASCII code of
the letters of the alphabet (both uppercase and lowercase letters,
since they have different ASCII codes):

\begin{center}
\begin{tabular}{ l r l r l r l r l r l r }
A & 65 \ \ \ \ \ \ & B & 66 \ \ \ \ \ \ & C & 67 \ \ \ \ \ \ & D & 68 \ \ \ \ \ \ & E & 69 \ \ \ \ \ \ & F & 70 \\
G & 71 \ \ \ \ \ \ & H & 72 \ \ \ \ \ \ & I & 73 \ \ \ \ \ \ & J & 74 \ \ \ \ \ \ & K & 75 \ \ \ \ \ \ & L & 76 \\
M & 77 \ \ \ \ \ \ & N & 78 \ \ \ \ \ \ & O & 79 \ \ \ \ \ \ & P & 80 \ \ \ \ \ \ & Q & 81 \ \ \ \ \ \ & R & 82 \\
S & 83 \ \ \ \ \ \ & T & 84 \ \ \ \ \ \ & U & 85 \ \ \ \ \ \ & V & 86 \ \ \ \ \ \ & W & 87 \ \ \ \ \ \ & X & 88 \\
Y & 89 \ \ \ \ \ \ & Z & 90 \ \ \ \ \ \ & \\
 \\
a & 97 \ \ \ \ \ \ & b & 98 \ \ \ \ \ \ & c & 99 \ \ \ \ \ \ & d & 100 \ \ \ \ \ \ & e & 101 \ \ \ \ \ \ & f & 102 \\
g & 103 \ \ \ \ \ \ & h & 104 \ \ \ \ \ \ & i & 105 \ \ \ \ \ \ & j & 106 \ \ \ \ \ \ & k & 107 \ \ \ \ \ \ & l & 108 \\
m & 109 \ \ \ \ \ \ & n & 110 \ \ \ \ \ \ & o & 111 \ \ \ \ \ \ & p & 112 \ \ \ \ \ \ & q & 113 \ \ \ \ \ \ & r & 114 \\
s & 115 \ \ \ \ \ \ & t & 116 \ \ \ \ \ \ & u & 117 \ \ \ \ \ \ & v & 118 \ \ \ \ \ \ & w & 119 \ \ \ \ \ \ & x & 120 \\
y & 121 \ \ \ \ \ \ & z & 122 \ \ \ \ \ \ & 
\end{tabular}
\end{center}
\vspace{0.1in}

Now let's convert the \quoted{The quick fox} message once more, but
this time we'll convert each letter to its corresponding ASCII code,
and then shift the letter by subtracting the number of spaces we want
to shift by. This leaves us with a new ASCII code that corresponds to
the encoded letter:

\begin{alignat}{3}
\quoted{T}\ -\ 3\ \Rightarrow & \quad\ \ 84\ -\ 3\ \Rightarrow && \quad\ \ 81\ \Rightarrow && \quad\ \quoted{Q} \nonumber \\
\quoted{h}\ -\ 3\ \Rightarrow & \quad\ 104\ -\ 3\ \Rightarrow && \quad\ 101\ \Rightarrow && \quad\ \quoted{e} \nonumber \\
\quoted{e}\ -\ 3\ \Rightarrow & \quad\ 101\ -\ 3\ \Rightarrow && \quad\ \ 98\ \Rightarrow && \quad\ \quoted{b} \nonumber \\
\quoted{q}\ -\ 3\ \Rightarrow & \quad\ 113\ -\ 3\ \Rightarrow && \quad\ 110\ \Rightarrow && \quad\ \quoted{n} \nonumber \\
\quoted{u}\ -\ 3\ \Rightarrow & \quad\ 117\ -\ 3\ \Rightarrow && \quad\ 114\ \Rightarrow && \quad\ \quoted{r} \nonumber \\
\quoted{i}\ -\ 3\ \Rightarrow & \quad\ 105\ -\ 3\ \Rightarrow && \quad\ 102\ \Rightarrow && \quad\ \quoted{f} \nonumber \\
\quoted{c}\ -\ 3\ \Rightarrow & \quad\ \ 99\ -\ 3\ \Rightarrow && \quad\ \ 96\ \Rightarrow && \quad\ \quoted{z} \nonumber \\
\quoted{k}\ -\ 3\ \Rightarrow & \quad\ 107\ -\ 3\ \Rightarrow && \quad\ 104\ \Rightarrow && \quad\ \quoted{h} \nonumber \\
\quoted{f}\ -\ 3\ \Rightarrow & \quad\ 102\ -\ 3\ \Rightarrow && \quad\ \ 99\ \Rightarrow && \quad\ \quoted{c} \nonumber \\
\quoted{o}\ -\ 3\ \Rightarrow & \quad\ 111\ -\ 3\ \Rightarrow && \quad\ 108\ \Rightarrow && \quad\ \quoted{l} \nonumber \\
\quoted{x}\ -\ 3\ \Rightarrow & \quad\ 120\ -\ 3\ \Rightarrow && \quad\ 117\ \Rightarrow && \quad\ \quoted{u} \nonumber
\end{alignat}

Note that the number ranges in the ASCII table go from 65 to 90 for
uppercase letters, and 97 to 122 for lowercase letter. All codes
outside of these ranges are not codes for letters (for example, the
code for the right square bracket character [ is 91.

Whenever a shift causes us to fall outside of the ranges for uppercase
or lowercase letters, we must \quoted{wrap around} to the other end of
the range. For example, when we shift the letter \quoted{b} which has
an ASCII code of 98 by minus 3, we should result in 121 (and NOT
95). Think of the ranges as being continous ranges that restart when
ever they reach their end: 97, 98, 99, ..., 121, 122, 97, 98, 99, ...,
and so on.

If you'd like to play around with a complete Caesar cipher
implmenetation, you can head over to
\href{https://cryptii.com/pipes/caesar-cipher}{this site}. The site
gives you an option to shift by different numbers (both positive and
negative) by updating the \quoted{Shift} value in the center of the
page. If you'd like to learn more about Caesar cipher, I recommend
visiting the \href{https://en.wikipedia.org/wiki/Caesar_cipher}
{Wikipedia} which has additional examples and information about its
history:

\begin{displayquote}
\setstretch{1.5}
\quoted{In cryptography, a Caesar cipher, also known as Caesar's
cipher, the shift cipher, Caesar's code or Caesar shift, is one of the
simplest and most widely known encryption techniques. It is a type of
substitution cipher in which each letter in the plaintext is replaced
by a letter some fixed number of positions down the alphabet. For
example, with a left shift of 3, D would be replaced by A, E would
become B, and so on. The method is named after Julius Caesar, who used
it in his private correspondence.} \footnotesize{\href{https://en.wikipedia.org/wiki/Caesar\_cipher}{https://en.wikipedia.org/wiki/Caesar\_cipher}}
\end{displayquote}
\begin{center}
\vspace{0.2in}
\includegraphics[scale=0.5]{Caesar_cipher}
\vspace{0.2in}
\end{center}

## Instructions

Your web application should let a user enter a message which they want
to encode along with the shift value which can either be positive or
negative by adding a minus sign before it. You should use a
\code{<form>} that accepts the user's input and sends it in a
\code{POST} request. When the user submits their message, you should
encode it by shifting all letters by the shift value they provided,
then show them the encoded message.

This application is able to both encode and decode messages. All the
user has to do to decode a message that was shifted by 3 spaces is
provide -3 as the shift value.

## Tips

- The \code{int} function can convert negative numbers:
  \code{int("-3") == -3}
- Use the \code{chr} function to convert a number to a letter (ASCII
  code to letter): \code{chr(97) == "a"}
- Use the \code{ord} function to convert a letter to a number (letter
  to ASCII code): \code{ord("a") == 97}
- In order to determine if you need to \quoted{wrap around} to the
  beginning or the end of an ASCII code range, you should check if the
  number you \quoted{shifted} to falls outside of its corresponding
  letter range.

  Lowercase letters should fall within 97 to 112. Uppercase letters
  should fall within 65 to 90.  So if you're shifting the letter
  \quoted{b} by -3, you'd get 98 - 3 = 95. Because we're working with
  a lowercase letter, we check that this result falls within the
  lowercase letter range or 97 - 112, and we can see that it does not,
  so we would have to wrap around to the end to get the correct result
  of 121.

  Calculating the wrap around value will require doing some
  math/logic. The math/logic you use may change depending on if you
  need to go from the beginning to the end (65 to 90, 97 to 122) or
  the end back to the beginning (90 to 65, 122 to 97)
