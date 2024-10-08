# Fraud Detector

## Overview

The Fraud Detector project aims to build a robust system for identifying fraudulent transactions using machine learning techniques. The system leverages various classification algorithms, including Random Forest, Decision Trees, and Logistic Regression, to accurately classify transactions as either fraudulent or legitimate.

## Features

- **Data Preprocessing:** Handles missing values, encodes categorical variables, and scales numerical features.
- **Model Training:** Utilizes multiple machine learning models and hyperparameter tuning to enhance performance.
- **Model Evaluation:** Includes metrics such as accuracy, classification report, and confusion matrix to evaluate model performance.
- **API Integration:** Exposes a RESTful API using Django REST Framework for predicting fraud on transaction data.
- **Interactive Testing:** Provides a Postman collection for testing API endpoints.

## Technologies Used

- **Python**: Primary programming language for data processing and machine learning.
- **Scikit-learn**: For implementing and evaluating machine learning models.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical operations.
- **Django REST Framework**: For creating and managing the RESTful API.
- **Joblib**: For saving and loading trained models.
- **Postman**: For API testing and interaction.

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>

2. **Navigate to Project Directory:**
    cd fraud_detector

3. **Create and Activate a Virtual Environment:**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

4. **Create and Activate a Virtual Environment:**
    pip install -r requirements.txt

5. **Apply Migrations:**
    python manage.py migrate

6. **python manage.py runserver:**
    python manage.py runserver

7. **Test the API:**
    Use Postman to send a POST request to the /predict/ endpoint with the required JSON payload for fraud prediction.

**Example Request**
***Endpoint***
POST /predict/

**Request Body**

{
  "type": "TRANSFER",
  "amount": 1000.0,
  "oldbalanceOrg": 5000.0,
  "newbalanceOrig": 4000.0,
}

Response

{
  "prediction": 1  // 1 for Fraud, 0 for Non-Fraud
}
