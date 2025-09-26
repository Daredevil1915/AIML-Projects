from flask import Flask, request, render_template
import numpy as np
import pickle

# WSGI callable for EB
application = Flask(__name__)

# Load saved model
model = pickle.load(open("model.pkl", "rb"))

@application.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            # Get form values
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            DC = float(request.form.get('DC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Prepare input and predict
            input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, Classes, Region]])
            prediction = model.predict(input_data)
            result = prediction[0]

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', results=result)

if __name__ == "__main__":
    # Only for local testing
    application.run(debug=True, host='0.0.0.0', port=5000)
