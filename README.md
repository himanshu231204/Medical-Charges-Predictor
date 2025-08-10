
# Medical Charges Predictor

A simple web application that predicts medical insurance charges using a Linear Regression model. Users can input personal details such as age, BMI, smoking status, number of children, gender, and region to estimate their insurance cost.

## Features

- Input form with relevant medical and demographic features
- Uses a trained Linear Regression model for prediction
- Clean and responsive UI with 2-column layout for inputs
- Shows predicted medical charges instantly after submission

## Technologies Used

- **Frontend:** HTML, CSS (flexbox for layout)
- **Backend:** Python (Flask)
- **Machine Learning:** Scikit-learn Linear Regression model

## Installation & Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-charges-predictor.git
    cd medical-charges-predictor
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    flask run
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## Model Training

The Linear Regression model was trained using a dataset containing features like:

- Age (scaled)
- Gender (Is Female)
- BMI (scaled)
- Number of children (scaled)
- Smoking status
- Region (One-hot encoded)
- BMI category (One-hot encoded)

## File Structure

````

├── app.py                 # Flask backend application
├── model.pkl              # Saved trained Linear Regression model
├── templates/
│   └── index.html         # HTML template for the frontend form
├── static/
│   └── style.css          # Optional external stylesheet
├── requirements.txt       # Python dependencies
└── README.md

```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.

---

If you want me to help with the Flask backend code or training scripts, just ask!
```
