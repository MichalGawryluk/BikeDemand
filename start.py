import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
# plt.switch_backend('Qt4Agg')

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

desired_width: int = 320
pd.set_option('display.width', desired_width)
# np.set_printoption(linewidth=desired_width)
pd.set_option('display.max_columns', 15)


def data_load(path):
    data = pd.read_csv(path)
    return data


def data_simple_eda(data):
    print("######## EDA ##", data.name)

    print(data.isna().sum())
    print(data.dtypes)
    print(data.describe())


def pre_processing_train(trainset):
    trainset.datetime = pd.to_datetime(trainset.datetime)


def split_train_test(split_par, df):
    split_id = round(len(df) * split_par)
    train = df.loc[:split_id, :]
    test = df.loc[split_id + 1:, :]
    return train, test


def benchmark_model(xors, ys):
    lm = LinearRegression()
    lm.fit(xors, ys)
    return lm


def evaluate(model, testset, ys):
    preds = model.predict(testset)
    r2 = r2_score(ys, preds)
    mae = mean_absolute_error(ys, preds)
    return print(model, "R2: ", r2, "MAE: ", mae)


if __name__ == '__main__':
    train = data_load('./bike-sharing-demand/train.csv')
    train.name = 'TRAIN'
    print(train)

    test = data_load('./bike-sharing-demand/test.csv')
    test.name = 'TEST'
    print(test)

    data_simple_eda(train)
    data_simple_eda(test)

    pre_processing_train(train)

    train, test = split_train_test(0.2, train)

    regresors = ["season", "workingday", "holiday", "weather", "temp", "atemp", "humidity", "windspeed"]
    target = ["count"]

    X = train[regresors]
    y = train[target]
    X_test = test[regresors]
    y_test = test[target]

    bm = benchmark_model(X, y)
    evaluate(bm, X_test, y_test)

    # print(pd.to_datetime(train.datetime) - pd.DateOffset(day=1))