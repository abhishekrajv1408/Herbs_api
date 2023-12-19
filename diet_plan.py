import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def herb(x_test):
    data = pd.read_csv("herbs.csv")
    from sklearn.model_selection import train_test_split
    x = data.drop("effect", axis = 1)
    y = data["effect"]
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, random_state = 2, test_size = .80)
    # Using Linear Regression\
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(xtrain, ytrain)
    y_pre = int(reg.predict(x_test))
    # data = np.array["Not harm full for human","Good for small baby", "Good for Adults", "Harmfull for Human body"]
    # return data[y_pre]
    return y_pre