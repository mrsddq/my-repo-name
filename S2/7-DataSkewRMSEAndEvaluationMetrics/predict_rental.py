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

# y = mx + C
# label = m(feature) + C
# m -> coefficient, C -> intercept
#  price = cofficient1(rooms) + coefficient2(sqft) + intercept
#  price = 1900(rooms) + 

# retrieve coefficients and intercept
print("Coefficient from Trained Model", model.coef_)
print("Intercept from Trained Model", model.intercept_)

# prediction for the dataset
print("Actual Rental Price for rooms", X_test[0][0], "with sqft", X_test[0][1], "is", y_test[0])

predictedRental = model.predict(np.array([[X_test[0][0],X_test[0][1]]]))

print("Predicted Rental Price for rooms =", X_test[0][0], "with sqft", X_test[0][1], "is =", predictedRental)

# # get the user input for number of rooms and squarefoot
# rooms = int(input("Enter number of rooms: "))
# sqft = int(input("Enter square footage: "))

# # predict the rental price based on user input
# user_input = np.array([[rooms, sqft]])
# predicted_price = model.predict(user_input)
# print(f"Predicted Rental Price for {rooms} rooms with {sqft} sqft is: {predicted_price[0]}")