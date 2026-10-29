# import the Flask library into this file
from flask import Flask

# create a new Flask app named "app"
app = Flask(__name__)

# create a homepage for our Flask app (website)
@app.route('/')
def Index():
    return "Welcome to the homepage!"

if __name__ == '__main__':
    app.run(debug = True)