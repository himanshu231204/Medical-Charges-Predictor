from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("charges_model.pkl", "rb"))

# Your training feature order (replace with actual names or keep order same as training)
feature_names = [
    "feat1", "feat2", "feat3", "feat4", "feat5",
    "feat6", "feat7", "feat8", "feat9", "feat10",
    "feat11", "feat12", "feat13"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()

        # Ensure we have all features in correct order
        final_features = []
        for feat in feature_names:
            value = float(data.get(feat, 0))  # default 0 if missing
            final_features.append(value)

        # Convert to numpy array with correct shape
        features_array = np.array([final_features])  # shape (1, 13)

        # Make prediction
        prediction = model.predict(features_array)

        return render_template('index.html', prediction_text=f"Predicted value: {prediction[0]:.2f}")

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render's PORT environment variable
    app.run(host="0.0.0.0", port=port)
