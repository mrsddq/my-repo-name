# Rental Price Prediction using Linear Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Load rental data from CSV file."""
    return pd.read_csv(filepath)

def prepare_features(data):
    """Prepare features and labels."""
    X = data[['rooms', 'sqft']].values
    y = data['price'].values
    return X, y

def train_model(X_train, y_train):
    """Train linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_price(model, rooms, sqft):
    """Predict rental price for given rooms and sqft."""
    user_input = np.array([[rooms, sqft]])
    return model.predict(user_input)[0]

def main():
    # Load and prepare data
    data = load_data('data/housing_1000.csv')
    X, y = prepare_features(data)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = train_model(X_train, y_train)

    # Model details
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)

    # Test prediction
    print(f"Actual Rental Price for rooms {X_test[0][0]} with sqft {X_test[0][1]} is {y_test[0]}")
    predicted = predict_price(model, X_test[0][0], X_test[0][1])
    print(f"Predicted Rental Price for rooms = {X_test[0][0]} with sqft {X_test[0][1]} is = {predicted}")

    # User input prediction
    try:
        rooms = int(input("Enter number of rooms: "))
        sqft = int(input("Enter square footage: "))
        user_pred = predict_price(model, rooms, sqft)
        print(f"Predicted Rental Price for {rooms} rooms with {sqft} sqft is: {user_pred}")
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()