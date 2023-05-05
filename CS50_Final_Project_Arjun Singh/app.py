import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd



# Configure application
app = Flask(__name__)

TERMS=[
    "Fall",
    "Winter",
    "Spring",
    "Summer"
]

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///grades.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods = ["GET","POST"])
@login_required
def mainpage():
    if request.method=="POST":
        return apology("")
    else:
        return render_template("mainpage.html")


@app.route("/electrical", methods=["GET", "POST"])
@login_required
def add():
    """Buy shares of stock"""
    # query search for a stock
    #return apology("Page under construction")
    if request.method == "POST":
        user_id = session["user_id"]
        #username= str(db.execute("SELECT username FROM users WHERE id=?", user_id))
        course_input= request.form.get("course")
        credit_hours_input= int(request.form.get("credit_hours"))
        term_input= str(request.form.get("term"))
        year_input= int(request.form.get("year"))

        if not credit_hours_input > 0:
            return apology("please select valid credit hours",)
        elif term_input=="term":
            return apology("please select a term",)
        elif not year_input >0:
            return apology("please select a valid year")

#        rows = db.execute("SELECT cash FROM users WHERE id=?", user_id)
 #       cash = rows[0]["cash"]


        #db.execute("UPDATE users SET cash=? WHERE id=?", cash_left, session["user_id"])
        db.execute("INSERT INTO courses(user_id, course, credit_hours, term,year) VALUES(?,?,?,?,?)", user_id, course_input, credit_hours_input, term_input, year_input)

        flash("Added!")
        return redirect("/electrical")

    else:
        database1 = db.execute("SELECT * FROM courses WHERE user_id=?", session["user_id"])
        rows1 = db.execute("SELECT * FROM years WHERE user_id=?", session["user_id"])
        start_year=rows1[0]["start_year"]
        end_year=rows1[0]["end_year"]
        start_term=rows1[0]["first_term"]
        end_term=rows1[0]["last_term"]
        return render_template("fouryearplan.html", terms=TERMS,start_year=int(start_year), end_year=int(end_year), start_term=start_term, end_term=end_term,schedule=database1 )





@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    database = db.execute("SELECT * FROM courses WHERE user_id=?", session["user_id"])
    return render_template("history.html", history = database)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username ha ha", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        rows1 = db.execute("SELECT * FROM years WHERE user_id=?", session["user_id"])
        if len(rows1)!= 1:
            return redirect("/index")
        else:
            return redirect("/")
        # Redirect user to home page


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")
        major_input = request.form.get("major")



        #Ensure username was submitted
        if not username:
            return apology("must provide a username", 400)
        elif not password:
            return apology("must provide a password", 400)
        elif not confirm_password:
            return apology("please fill in all fields", 400)
        elif not major_input:
            return apology("Please select a major", 400)



        rows = db.execute("SELECT * FROM users WHERE username =?", username)
        # Ensure username does not exist
        if len(rows) == 1:
            return apology("username is already taken, please choose another username")

        #Ensure password match
        if password != confirm_password:
            return apology("Password's do not match, Please try again")

        hashed_value_password = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash, major) VALUES(?, ?, ?)", username, hashed_value_password, major_input)

        rows2 = db.execute("SELECT * FROM users WHERE username =?", username)

        session["user id"]= rows2[0]["id"]
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/remove", methods=["GET", "POST"])
@login_required
def delete():
    """Sell shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]

        remove_course_input= str(request.form.get("course_remove"))
        remove_term_input = request.form.get("remove_term")
        remove_year_input = request.form.get("remove_year")

        if remove_term_input=="term":
            return apology("please select a term",)

        rows2 = db.execute("SELECT course FROM courses WHERE course=? AND term=?", remove_course_input, remove_term_input)
        if len(rows2) ==0:
            return apology("class with this term doesn't exist")

        rows3 = db.execute("SELECT * FROM courses WHERE course=? AND term=? AND year=?",remove_course_input, remove_term_input, remove_year_input)
        if len(rows3) == 0:
            return apology("class with this year doesn't exist")


        db.execute("DELETE FROM courses WHERE course=? AND term=? AND year=?", remove_course_input, remove_term_input, remove_year_input)
        flash("removed")
        return redirect("/remove")

    else:
        rows = db.execute("SELECT course FROM courses WHERE user_id=:user_id", user_id=session["user_id"])
        return render_template("remove.html",terms= TERMS, courses = [ row["course"] for row in rows ])
