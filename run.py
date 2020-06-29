import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # Main Page With Instructions
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    # Display Chat Messages
    return "Hi " + username


@app.route('/<username>/<message>')
def send_message(username, message):
    # Create a New Message And Redirect Back To The Chat Page
    return "{0}: {1}".format(username, message)


if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
