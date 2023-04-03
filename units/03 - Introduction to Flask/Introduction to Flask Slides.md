---
theme: css/custom-simple.css
highlightTheme: css/layout.css
---

<!-- .slide: class="center" -->

# Intermediate Python

### Unit 3: Introduction to Flask

---

<!--
paginate: true
footer: 'Unit 3: Introduction to Flask'
-->

## Overview

<span class="centered narrower">

- What is Flask?
- Why are we learning this?
- The Internet, aka "the web"
- Writing Flask applications

</span>

---

# What is Flask?

---

Flask is a Python library.

---

<span class="center wide">

Flask is a library that lets us create **web applications** and **websites/webpages**.

</span>

---

<span class="center narrow">

Flask is a web framework.

</span>

---

<span class="center narrow">

Flask helps us build web servers.

</span>

---

<span class="center narrow">

Flask helps us build web servers that power our web applications.

</span>

---

## A note on terminology

<span class="center wide">

The terms **web application**, **website**, and **webpage** are all interchangeable and refer to a website that is accessed with a web browser.

</span>

---

# Why are we learning this?

---

## Why are we learning this?

<span class="center narrow">

Much of our world is powered by the web.

</span>

---

## Why are we learning this?

<span class="center wide">

Even when we're not browsing _the web_ on our _browsers_, we're likely on the web.

</span>

---

## Why are we learning this?

<span class="center narrow">

Everything is connected to the web: your phone, your watch, even your fridge might even be connected to the web.

</span>

---

## Why are we learning this?

<span class="center narrow">

But the primary use of the web is still the usage of webpages, and this is what we'll be learning about.

</span>

---

## Why are we learning this?

<span class="center narrow">

Being able to create programs that rely on _the web_ or _networking_ is an important part of being a software engineer.

</span>

---

# The Internet

---

## What is The Internet?

<span class="center narrow">

The Internet is a global network of billions of computers and electronic devices that are able to talk to each other.

</span>

---

## Talking to each other

<span class="center narrow">

What is meant by "talking to each other" is simply the act of sending and receiving messages.

</span>

---

## Talking to each other

<span class="center narrow">

The first computer sends a **request** for some data and the second computer **responds** to the request.

</span>

---

## Terminology

<span class="centered narrower">

- **Request**: a message sent by a computer, the sender, to another computer, the receiver.
- **Response**: a response to a message sent back from the receiver to the sender.

</span>

---

<span class="centered">
<img src="Request Response.png" />
</span>

---

# Let's jump into the code

---

## Sample Flask application

```python
import flask

app = flask.Flask(__name__)

@app.get("/")
def index():
    return "Hello, world"

app.run()
```

---

## Let's break this down

<pre><code>import flask

app = flask.Flask(__name__)

@app.get("/")
def index():
    return "Hello, world"

app.run()</code></pre>

---

## Imports

<pre><code><span class="highlight">import flask</span>

app = flask.Flask(__name__)

@app.get("/")
def index():
    return "Hello, world"

app.run()</code></pre>

---

## Using imported code

<pre><code>import flask

app = <span class="highlight">flask.Flask(__name__)</span>

@app.get("/")
def index():
    return "Hello, world"

app.run()</code></pre>

---

## <code>\_\_name\_\_</code>

<pre><code>import flask

app = flask.Flask(<span class="highlight">__name__</span>)

@app.get("/")
def index():
    return "Hello, world"

app.run()</code></pre>

---

## Creating an application

<pre><code>import flask

<span class="highlight">app = flask.Flask(__name__)</span>

@app.get("/")
def index():
    return "Hello, world"

app.run()</code></pre>

---

## Running an application

<pre><code>import flask

app = flask.Flask(__name__)

@app.get("/")
def index():
    return "Hello, world"

<span class="highlight">app.run()</span></code></pre>

---

## Functions

<pre><code>import flask

app = flask.Flask(__name__)

@app.get("/")
<span class="highlight">def index():
    return "Hello, world"</span>

app.run()</code></pre>

---

<span class="center wide">

Whatever our function returns will be the response sent back to the client.

</span>

---

<span class="center wide">

Whatever our function returns will be what is displayed in our browser.

</span>

---

## Decorators

<pre><code>import flask

app = flask.Flask(__name__)

<span class="highlight">@app.get("/")</span>
def index():
    return "Hello, world"

app.run()</code></pre>

---

## Decorators

Decorators allow us to add functionality to out functions.

---
