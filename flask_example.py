#Creating dependencies
from flask import Flask

# Creates a new flask app instance 
app = Flask(__name__)

# Creating a Flask Route
@app.route('/')
def hello_world():
    return 'Hello world'
# Tells the computer to run after. 
if __name__=='__main__':
    app.run()