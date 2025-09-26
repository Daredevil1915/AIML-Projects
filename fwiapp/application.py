from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("Scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            features = [
                float(request.form["Temperature"]),
                float(request.form["RH"]),
                float(request.form["Ws"]),
                float(request.form["Rain"]),
                float(request.form["FFMC"]),
                float(request.form["DMC"]),
                float(request.form["ISI"]),
                int(request.form["Classes"]),
                int(request.form["Region"])
            ]
            input_df = pd.DataFrame([features], columns=[
                'Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region'
            ])
            input_scaled = scaler.transform(input_df)
            prediction = model.predict(input_scaled)[0]
            result = float(prediction)
            result = max(0, result)

        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("home.html", results=result)
if __name__ == "__main__":
    app.run(debug=True)
