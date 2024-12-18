import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


data = pd.read_csv("house_prices.csv")


def main():
    user_input = float(input("input Area: "))
    print(predict(user_input))

    print(f"Model R2 Score: {model_test()}")

    print_model_details()


msk = np.random.rand(len(data)) < 0.8
train = data[msk]
test = data[~msk]

train_x = np.asanyarray(train[["Area"]])
train_y = np.asanyarray(train[["Price"]])
model = LinearRegression()
model.fit(train_x, train_y)


plt.scatter(train_x, train_y)
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()
plt.plot(train_x, model.coef_[0][0] * train_x + model.intercept_[0])
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()


def predict(user_input):
    result = model.predict([[user_input]])
    return f"Predicted price: {result[0][0]}"


def model_test():
    test_x = np.asanyarray(test[["Area"]])
    test_y = np.asanyarray(test[["Price"]])
    test_y_ = model.predict(test_x)
    return r2_score(test_y, test_y_)


def print_model_details():
    print(f"Model Coefficient: {model.coef_[0][0]}")
    print(f"Model Intercept: {model.intercept_[0]}")


if __name__ == "__main__":
    main()
