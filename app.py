from flask import Flask, request, jsonify
import numpy as np
import joblib
import pandas as pd

# Load trained pipeline
pipeline = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert dict -> DataFrame
        import pandas as pd
        X = pd.DataFrame([data["features"]])  

        prediction = pipeline.predict(X)
        return jsonify({"predicted_price": float(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)

