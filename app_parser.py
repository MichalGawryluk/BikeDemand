import pickle

from start import pre_processing_train, fe_datetime, fe_ohe_categories, fe_manual_rushhours


def parsedata(data):
    pre_processing_train(data)
    fe_datetime(data)
    data, ohe_regs = fe_ohe_categories(data, ["season", "weather"])
    fe_manual_rushhours(data)

    simple_regresors = ["workingday", "holiday", "temp", "atemp", "humidity", "windspeed"]
    time_regrosors = ["hour", "day", "week", "weekday", "month", "year"]
    manual_regs = ["rushhour"]
    regresors = simple_regresors + time_regrosors + ohe_regs + manual_regs

    datamodelready = data[regresors]

    #Add oheregs misings
    with open("ohe_regs.pkl", "rb") as f:
        oheregm = pickle.load(f)

    missing_ohe = list(set(oheregm)  - set(ohe_regs) )
    for m in missing_ohe:
        datamodelready[m] = 0

    return datamodelready
