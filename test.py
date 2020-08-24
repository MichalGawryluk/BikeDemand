import glob
import json

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

from app_parser import parsedata
from start import data_load, pre_processing_train, fe_datetime, fe_ohe_categories, split_train_test

singledatapoint = json.dumps({"0": {"datetime": "2011-07-01 10:00:00", "season": 3,
                                    "holiday": 1, "workingday": 0, "weather": 4, "temp": 0.23,
                                    "atemp": 0.19, "humidity": 0.2, "windspeed": 0.5}})
jsonread = pd.read_json(singledatapoint, orient='index', convert_dates=['dteday'])


def test_data_load():
    df = data_load('./bike-sharing-demand/train.csv')
    assert isinstance(df, pd.DataFrame)


def test_datetime_format():
    df = data_load('./bike-sharing-demand/train.csv')
    pre_processing_train(df)
    assert is_datetime64_any_dtype(df.datetime)


def test_fe_ohe_categories():
    df = data_load('./bike-sharing-demand/train.csv')
    _, ohe_list = fe_ohe_categories(df, ["season", "weather"])
    assert len(ohe_list) == 8


def test_fe_datetime():
    df = data_load('./bike-sharing-demand/train.csv')
    len_org = len(df.columns)
    pre_processing_train(df)
    fe_datetime(df)
    assert len_org + 6 == len(df.columns)


def test_split():
    df = data_load('./bike-sharing-demand/train.csv')
    tr, te = split_train_test(0.2, df)
    assert len(df) == len(tr) + len(te)


def test_parsedata_n_of_regresors():
    X = parsedata(jsonread)
    assert len(X.columns) == 21


def test_start_all_pickles_dump():
    pickle_list = []
    for file in glob.glob("*.pkl"):
        pickle_list.append(file)
    assert len(pickle_list) == 4
