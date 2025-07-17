from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Collect form data
        data = CustomData(
            specific_gravity=float(request.form.get('specific_gravity')),
            ph_level=float(request.form.get('ph_level')),
            osmolality=float(request.form.get('osmolality')),
            conductivity=float(request.form.get('conductivity')),
            urea_concentration=float(request.form.get('urea_concentration')),
            calcium_concentration=float(request.form.get('calcium_concentration'))
        )

        # Convert data to DataFrame for prediction
        pred_df = data.get_data_as_data_frame()

        # Create prediction pipeline instance

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        predicted_class = int(results[0] >= 0.5)  # 1 if >= 0.5 else 0

    return render_template('home.html', results=predicted_class)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)