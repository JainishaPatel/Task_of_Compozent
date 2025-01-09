from flask import Flask, request, render_template
import pickle   # To load the saved machine learning model and encoder.
import pandas as pd

app = Flask(__name__)

# Load the trained model and crop encoder

with open('crop_1_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('crop_1_encoder.pkl', 'rb') as f:   # The label encoder (crop_1_encoder.pkl) to convert numeric predictions back to crop names.   
    crop_encoder = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    

    # Create a dataframe for prediction with all required features
    input_data = pd.DataFrame([[temperature, humidity]], columns=['temperature', 'humidity'])

    # Predict the crop index (numeric label) using the trained model
    crop_index = model.predict(input_data)[0]

    # Use the label encoder to convert the numeric index back to a crop name
    crop_name = crop_encoder.inverse_transform([crop_index])[0]

    # Return the result to be rendered on the page
    return render_template('index.html', prediction=crop_name)

if __name__ == '__main__':
    app.run(debug=True)
