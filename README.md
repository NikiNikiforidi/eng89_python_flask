# Model View Controller (MVC) with Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps 


### Let's see how we use python flask t0 interact with our browser
- Create a file called app.py

**flask run** : is the command used to run, in terminal
- (flask is controlling the behaviour of the browser)

- Install flask: pip install flask in terminal
```
 from flask import Flask
``` 
- We have to create an object of this class
```
 app = Flask(__name__) # Creating an app instance
```

### Let's connect a function to our internet browser.
- We want this file to open a browser. Let's create a function to link our home/default page

```
 @app.route("/")

 def index():
     return " Welcome to Engineering 89 DevOps team"
```
- Let's create a welcome page
```
 @app.route("/welcome/")
 def welcome():
     return "<h1> Welcome page for Flask app </h1> "
```

- Created a login page
```
 @app.route("/login/")

 def login():
     return" <h1> You are currently at the login page </h1> <h2> Please login: </h2> "
```

- ---------------------------------------------

### Redirecting user
**What if the login page is unavailable?**

-  We should to re-direct the users if they visit login page that doesn't exist

- redirect and url_for we need to import
```
 from flask import Flask,redirect,url_for

 app = Flask(__name__)

 @app.route("/")

 def index():
     return " Welcome to Engineering 89 DevOps team"


 @app.route("/welcome/")
 def welcome():
     return "<h1> Welcome page for Flask app </h1> "
```

 - Would like to redirect to welcome page if login page is unavailable
```
 @app.route("/login/")

 def login():
     return redirect(url_for("welcome"))
```
 - Checks if you're running the file within the same file or if the file is being run somewhere else
 ```
 if __name__ == "__main__":
     app.run(debug=True)
```
- --------------------------------------------------


### Let's add our HTML file to redirect from Python flask to html. file
- We create a folder called templates to add some fancy stuff to our welcome page (using [Bootstrap](https://getbootstrap.com/))
- need to import render_template
- project folder ->(create directory) templates folder  -> welcome.html

```
from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")

def index():
    return " Welcome to Engineering 89 DevOps team"


@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

@app.route("/login/")

def login():
    return redirect(url_for("welcome"))
if __name__ == "__main__":
    app.run(debug=True)
```


```
 @app.route("/<username>/") # passing variable provided by the user in the browser
 def greet_user(username):
     return f"Welcome to flask web app dear {username}" # display the name back to user in the browser
```

- -------------------------------------------------------------------

- Created a new directory called templates and added `welcome.html` file

_ Most of the code was copied from bootstrap.
```


<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="UTF-8">
    <title>Engineering 89 DevOps</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

  <nav class="navbar navbar-dark bg-dark">
  <!-- Navbar content -->
</nav>


<nav class="navbar navbar-dark bg-primary">
  <!-- Navbar content -->
</nav>


<nav class="navbar navbar-light" style="background-color: #e3f2fd;">
  <!-- Navbar content -->
</nav>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar scroll</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarScroll">
      <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Link
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Link</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

</head>


<body>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>

<h2>Please login</h2>

<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>


</html>
```