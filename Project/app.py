"""
Bank Fund Prediction Web Application

This Flask application provides a web interface for predicting bank funds
using a pre-trained machine learning model. Users can input financial data
through a web form and receive predictions.

The application uses:
- Flask for the web framework
- Joblib for loading the serialized ML model
- NumPy for numerical operations
"""
from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained machine learning model
loaded_model = joblib.load('model.sav')

@app.route('/')
def index():
    """
    Render the main page of the application.
    
    Returns:
        Rendered HTML template for the index page
    """
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    """
    Make predictions using the loaded model.
    
    Args:
        to_predict_list (list): List of input features for prediction
        
    Returns:
        float: The predicted value
    """
    # Reshape input for model compatibility
    to_predict = np.array(to_predict_list).reshape(-1, 1)
    # Generate prediction using the loaded model
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle the prediction request from the form submission.
    
    Processes the form data, converts it to the appropriate format,
    makes a prediction, and returns the result.
    
    Returns:
        Rendered HTML template with prediction results
    """
    if request.method == 'POST':
        # Get form data as dictionary
        to_predict_list = request.form.to_dict()
        # Extract values from the dictionary
        list_to_predict_list = list(to_predict_list.values())
        # Convert string values to float
        to_predict_list = list(map(float, list_to_predict_list))
        
        # Get prediction from the model
        # Note: The commented code below was refactored into ValuePredictor function
        #to_predict = np.array(to_predict_list).reshape(-1, 1)
        #result = loaded_model.predict(to_predict)
        
        # Get the prediction and round to 2 decimal places
        result = round(float(ValuePredictor(to_predict_list)), 2)
        
        # Return the rendered template with prediction results
        return render_template("index.html", hasil=result, dana=list_to_predict_list)

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)