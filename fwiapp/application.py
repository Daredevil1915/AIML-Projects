import os
from flask import Flask, request, render_template
import numpy as np
import pickle

application = Flask(__name__)


script_dir = os.path.dirname(os.path.realpath(__file__))

model_path = os.path.join(script_dir, "model.pkl")


model = pickle.load(open(model_path, "rb"))


@application.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
   
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

            
            input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, Classes, Region]])
            scaled_data = scaler.transform(input_data)  # <-- THIS IS THE FIX
            prediction = model.predict(scaled_data)     # <-- Use the scaled data
            result = prediction[0]
            
          

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', results=result)

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5000)