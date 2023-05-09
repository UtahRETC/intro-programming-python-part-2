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

#### Query Parameters and Request Class In Flask

<span class="center wide">
<img src="assets/Flask Header.png" />
</span>

---

#### A Quick Review of URL's And Schemes

<span class="centered">
<img src="assets/Example Url.png" />
</span>

---

#### What Is HTTP/HTTPS?

<span class="centered">
<img src="assets/HTTP Request Example.png" />
</span>

---

#### Website Speak In HTTP

<span class="centered">
<img src="assets/Website Traffic.png" />
</span>

---

#### In Flask, We Access HTTP Requests With The `request` Class

`http://127.0.0.1:5000/hello?name=Brady`

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello') 
def hello():     
	name = request.args.get('name')     
	return "Hello, " + name

app.run()
```

**Notice that request.args is a dictionary! Remember those?**

```python
my_dictionary = {"name": "Brady"}
```

---

#### Request looks like this

<span class="centered">
<img src="assets/Chrome Request.png" />
</span>

---

#### Working With Multiple Arguments

<span class="centered">
<img src="assets/Query Param Example.png" />
</span>

```python

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello') 
def hello():     
	return "Here are all your args:" + str(request.args)

app.run()
```

**Looks similar to**

```python
my_dictionary = {"name": "Brady", "age": 31, "city": "Salt Lake City"}
```

---

#### Handling User Input with Query Parameters

```python
from flask import Flask, request  

app = Flask(__name__)  

@app.route('/greet') 
def greet():     
	name = request.args.get('name')  
	if name:
		return "Hello, " + {name}
	else:
		return 'Please enter your name.'

app.run()
```

---

#### Query parameters are Often Used to Filter, Sort or Search For Data

```python

from flask import Flask, request

app = Flask(__name__)

# A list of data in JSON format
people = [
    {"name": "Brady", "age": 31},
    {"name": "Marcos", "age": 31},
    {"name": "Nephi", "age": "??"},
]

# A route that filters the data by a 'name' query parameter
@app.route('/people')
def filter_people():
    # Get the 'name' query parameter from the URL
    name = request.args.get('name')
    
    if name is None:
        return str(people)

    # Filter the data by name, if name is provided, using a loop
    filtered_people = []
    for person in people:
        if person['name'] == name:
            filtered_people.append(person)


    return str(filtered_people)

app.run(debug=True)

# http://localhost:5000/people?name=John
```
