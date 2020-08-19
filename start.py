import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

desired_width=320
pd.set_option('display.width', desired_width)
#np.set_printoption(linewidth=desired_width)
pd.set_option('display.max_columns', 15)


def data_load(path):
    data = pd.read_csv(path)
    return data


if __name__ == '__main__':
    train = data_load('./bike-sharing-demand/train.csv')
    print(train)

    test = data_load('./bike-sharing-demand/test.csv')
    print(test)

    print(train.isna().sum())
    print(train.dtypes)

    print(test.isna().sum())
    print(test.dtypes)

    print(train.describe())
    print(test.describe())

    #plt.hist(train.workingday)

    print(train.datetime)
    print(train.casual)

    print(train.casual[0] + train.registered[0], train['count'][0])

    print(pd.to_datetime(train.datetime) - pd.DateOffset(day=1))

    lm = LinearRegression()

    X = train[["season", "workingday", "holiday", "weather", "temp", "atemp", "humidity", "windspeed"]]
    y = train["count"]

    lm.fit(X, y)

    preds = lm.predict(X)
    print(r2_score(y, preds))
    print(mean_absolute_error(y, preds))


