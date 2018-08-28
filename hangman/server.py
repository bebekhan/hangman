"""Hangman."""
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Score

import urllib2


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

# @app.route('/register', methods=['GET'])
# def register_form():
#     """Show form for user signup."""
# return render_template("register.html")

@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # taking user email and password from form
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    user_name = request.form.get("name")

    # checking to see if user already exists in db.
    check_email = User.query.filter_by(email=user_email).first()
    #indexing into the form.

    if check_email:
        flash('Email already exists!')
        return redirect('/login')
        
    # if no user exists add to database.
    else:
        new_user = User(name=user_name, email=user_email, password=user_password) 
        #add user
        db.session.add(new_user)
        #commit this change
        db.session.commit()   

        flash("User {} added. Going forward please user your {} and password to login".format(user_name, user_email))
#should eventually be routed to /user page to create/view trips and activites
    # return render_template('user.html', user=new_user)
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login_form():
        """Show login form."""
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    email = request.form["email"]
    password = request.form["password"]

    # Query for email address in db
    user = User.query.filter_by(email=email).first()
    # check_user_password = User.quesy.filter_by(password=user_password).first()

    if not user:
        flash("No account exists!")
        return redirect("/register")
  
    if user.password != password:
        flash("Incorrect credentials. Please try again.")
        return redirect("/login")

#create a session for this user.
    session["user_id"] = user.user_id
    #flash message to inform user they are logged in.
    # flash("Successfully Logged In!")
    #once logged in, the user should be directed to their personal users page.
    return render_template("homepage.html", user=user)  

@app.route('/logout', methods=['GET'])
def logout():
    """Log user out of current session."""

    del session["user_id"]
    # flash("Logged Out.")
    return render_template("logout.html")

# @app.route('/user', methods=['GET'])
# def view_player_dashboard():
#     """View game score details for single user."""


@app.route('/gameboard', methods=['GET']) # API route
def populate_words_iteratively(word_list):
    req = urllib2.Request('http://app.linkedin-reach.io/words')
    response = urllib2.urlopen(req)
    the_page = response.read()



    return(wordlist)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(port=5000, host='0.0.0.0')   