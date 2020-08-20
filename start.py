import pandas as pd
import numpy as np
import datetime

# import matplotlib.pyplot as plt
# plt.switch_backend('Qt4Agg')

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

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


def fe_datetime(df):
    df["hour"] = train.datetime.dt.hour
    df["day"] = train.datetime.dt.day
    df["week"] = train.datetime.dt.week
    df["weekday"] = train.datetime.dt.weekday
    df["month"] = train.datetime.dt.month
    df["year"] = train.datetime.dt.year


def fe_ohe_categories(df, list_cat_vars):
    ohe_regresors = []
    for cv in list_cat_vars:
        ohe = pd.get_dummies(df[cv], prefix=cv)
        ohe_regresors += ohe.columns.values.tolist()
        df = pd.concat([df, ohe], axis=1)
    return df, ohe_regresors


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
    np.random.seed(1992)

    train = data_load('./bike-sharing-demand/train.csv')
    train.name = 'TRAIN'
    print(train)
    print(np.unique(train.season))

    test = data_load('./bike-sharing-demand/test.csv')
    test.name = 'TEST'
    print(test)

    data_simple_eda(train)
    data_simple_eda(test)

    pre_processing_train(train)

    fe_datetime(train)
    train, ohe_regs = fe_ohe_categories(train, ["season", "weather"])

    train, test = train_test_split(train, test_size=0.2)
    print(np.unique(train.season))

    simple_regresors = ["workingday", "holiday", "temp", "atemp", "humidity", "windspeed"]
    time_regrosors = ["hour", "day", "week", "weekday", "month", "year"]
    regresors = simple_regresors + time_regrosors + ohe_regs
    target = ["count"]

    X = train[regresors]
    y = train[target]
    X_test = test[regresors]
    y_test = test[target]

    bm = benchmark_model(X, y)
    evaluate(bm, X_test, y_test)

    # print(pd.to_datetime(train.datetime) - pd.DateOffset(day=1))
