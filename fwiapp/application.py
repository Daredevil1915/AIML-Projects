from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Create Flask app (Elastic Beanstalk looks for "application")
application = Flask(__name__)
app = application

# Load saved model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""

    if request.method == 'POST':
        try:
            # Get values from form
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Prepare input for model (must be 9 features)
            input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

            # Predict
            prediction = model.predict(input_data)
            result = prediction[0]

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', results=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
