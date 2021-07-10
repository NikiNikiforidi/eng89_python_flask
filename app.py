#
# # ### Let's see how we use python flask tp interact with our browser
# # - Create a file called app.py
#
# # - **flask run** : is the command used to run, in terminal
# # - (flask is controlling the behaviour of the browser)
#
# # - Install flask: pip install flask in terminal
# from flask import Flask
# # - We have to create an object of this class
# app = Flask(__name__) # Creating an app instance
#
#
# # #### Let's connect a function to our internet browser.
#
# # - We want this file to open a browser. Let's create a function to link our home/default page
#
#
# @app.route("/")
#
# def index():
#     return " Welcome to Engineering 89 DevOps team"
#
#
#
# # - Let's create a welcome page
#
# @app.route("/welcome/")
# def welcome():
#     return "<h1> Welcome page for Flask app </h1> "
#
#
# # - Created a login page
#
# @app.route("/login/")
#
# def login():
#     return" <h1> You are currently at the login page </h1> <h2> Please login: </h2> "


# - ---------------------------------------------

# - Comment everything out from above before running below

# #### Redirecting user
# - **What if the login page is unavailable?**

# -  We should to re-direct the users if they visit login page that doesn't exist

# - redirect and url_for we need to import

# from flask import Flask,redirect,url_for
#
# app = Flask(__name__)
#
#
# @app.route("/")
#
# def index():
#     return " Welcome to Engineering 89 DevOps team"
#
#
# @app.route("/welcome/")
# def welcome():
#     return "<h1> Welcome page for Flask app </h1> "
#
#
# # - Would like to redirects to welcome page if login page is unavailable
# @app.route("/login/")
#
# def login():
#     return redirect(url_for("welcome"))
#
# # Checks if you're running the file within the same file or if the file is being run somewhere else
# if __name__ == "__main__":
#     app.run(debug=True)
#
#
#
#


# - -----------------------------------------------
# - Comment everything out from above to run code below

# #### Let's add our HTML file to redirect from Python flask to html. file
# - We create a folder called templates to add some fancy stuff to our welcome page (using bootstrap 5)

# - project folder ->(create directory) templates folder  -> welcome.html

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


#
# @app.route("/<username>/") # passing variable provided by the user in the browser
# def greet_user(username):
#     return f"Welcome to flask web app dear {username}" # display the name back to user in the browser



