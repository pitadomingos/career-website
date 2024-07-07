# Import modules
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)