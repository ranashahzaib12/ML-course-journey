from flask import Flask
import os 

# Create an instance of the Flask class
app = Flask(__name__)

# Define a basic route for the home page
@app.route('/',methods=['GET'])
def home():
    return "Hello, World!"
  
# # Define another route for a custom page
# @app.route('/about')
# def about():
#     return "This is the About page."

# Run the app on the local development server
if __name__ == '__main__':
    app.run(debug=True,host ="0.0.0.0" ,port = 5000 ) # Host 0.0.0.0 is important 
