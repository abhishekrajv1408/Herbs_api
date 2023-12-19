import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Adulttration(x_test):
    data = pd.read_csv("Milk_testing.csv")
    x_data = data.drop("quality", axis = 1)
    y_data = data["quality"]
    from sklearn.linear_model import LogisticRegression
    LR = LogisticRegression()
    LR.fit(x_data, y_data)
    ans = LR.predict(x_test)
    return ans