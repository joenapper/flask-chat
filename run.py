import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    # Adds Messages To The Chat List
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    # Gets All Messages And Separates Them With a Br(Line Break)
    return "<br>".join(messages)


@app.route('/', methods=["GET", "POST"])
def index():
    # Main Page With Instructions

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"]) 

    return render_template("index.html")


@app.route('/<username>')
def user(username):
    # Display Chat Messages
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    # Create a New Message And Redirect Back To The Chat Page
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
