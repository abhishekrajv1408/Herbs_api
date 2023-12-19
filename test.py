import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("herbs.csv")
from sklearn.model_selection import train_test_split
x = data.drop("effect", axis = 1)
y = data["effect"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, random_state = 2, test_size = .80)
# Using Linear Regression\
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(xtrain, ytrain)
y_pre = int(reg.predict(xtest))
print(y_pre)