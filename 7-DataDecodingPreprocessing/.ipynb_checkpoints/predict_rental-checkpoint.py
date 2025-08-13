import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load data
rentalPD = pd.read_csv('data/housing_1000.csv')

#prepare the data
X = rentalPD[['rooms','sqft']].values  # features - rooms and sqft
y = rentalPD['price'].values           # label - price

# split for train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

# model training
model = LinearRegression().fit(X_train, y_train)

# retrieve coefficients and intercept
print("Coefficient from Trained Model", model.coef_)
print("Intercept from Trained Model", model.intercept_)

# prediction for the dataset
print("Actual Rental Price for rooms", X_test[0][0], "with sqft", X_test[0][1], "is", y_test[0])

predictedRental = model.predict(np.array([[X_test[0][0],X_test[0][1]]]))

print("Predicted Rental Price for rooms =", X_test[0][0], "with sqft", X_test[0][1], "is =", predictedRental)