# Energy Consumption Prediction Application

## Project Overview
This is a Flask-based web application designed to predict energy consumption levels (Low, Medium, High) for buildings based on various input parameters. It features a user-friendly interface with a dynamic background video and an animated building, providing an engaging user experience.

## overview
https://matiullah8008.pythonanywhere.com/

## Features
- **Energy Consumption Prediction**: Predicts energy consumption based on building type, square footage, occupancy, insulation, appliances, temperature, HVAC efficiency, energy sources, peak usage hours, and annual energy cost.
- **Interactive UI**: Modern and responsive design using Bootstrap.
- **Dynamic Background**: Features a looping background video (`Buildings.webm`) for visual appeal.
- **Building Animation**: An animated building grows in the background, adding a unique visual element.
- **Prediction Distribution**: Displays the percentage breakdown of past predictions (Low, Medium, High).
- **Recommendations**: Provides tailored recommendations based on the predicted energy consumption level.

## For Users: How to Use
1.  **Access the Application**: Once the application is running (your developer will provide the URL, usually `http://127.0.0.1:5000/`), open it in your web browser.
2.  **Enter Building Details**: Fill in the form fields with accurate information about the building.
3.  **Get Prediction**: Click the "Predict Energy Consumption" button.
4.  **View Results**: The page will update to show the predicted energy consumption level, along with relevant recommendations and a distribution of all past predictions.
5.  **Go Back**: Click "Go Back" to return to the input form.

## For Developers: Setup and Run

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1.  **Clone the repository** (if applicable, otherwise navigate to the project directory):
    ```bash
    cd C:\Users\Matiullah\Desktop\DS-project-Matiullah-266
    ```
2.  **Install dependencies**: All required Python packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ensure Model and Data Files are Present**: Make sure `energy_prediction_model .pkl` and `Energy_Consumption_Prediction.csv` are in the root directory.
4.  **Place Background Video**: Ensure `Buildings.webm` is located in the `static/` directory.

### Running the Application
To start the Flask development server:
```bash
python flask_app.py
```

The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

### Project Structure
```
C:/Users/Matiullah/Desktop/DS-project-Matiullah-266/
├───Energy_Consumption_Prediction.csv  # Dataset for training/analysis
├───energy_prediction_model .pkl       # Trained machine learning model
├───flask_app.py                       # Main Flask application logic
├───README.md                          # This documentation file
├───requirements.txt                   # Python dependencies
├───static/                            # Static assets (CSS, images, videos)
│   ├───Buildings.webm                 # Background video animation
│   └───style.css                      # Custom CSS styles
└───templates/                         # HTML templates
    └───index.html                     # Main and results page
```

## Technologies Used
- **Backend**: Python, Flask, joblib, pandas
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (for animation)
- **Machine Learning**: Scikit-learn (for model training, implied by `.pkl`)

## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.



## About the Author
This project was developed by Matiullah, a dedicated student of Data Science. It showcases practical application of machine learning for energy consumption prediction and web development skills using Flask.
