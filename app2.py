from flask import Flask, request, jsonify
from app_parser import parsedata
import json, pickle
import pandas as pd

app = Flask(__name__)


@app.route('/api/prediction/LM/', methods=['POST'])
def prediction():
    """

    Function run at each API call

    """

    """

    Function run at each API call

    """

    jsonfile = request.get_json()

    data = pd.read_json(json.dumps(jsonfile), orient='index', convert_dates=['dteday'])

    print(data)

    res = dict()

    modelfile = 'lm.pkl'
    model = pickle.load(open(modelfile, 'rb'))

    ypred = model.predict(parsedata(data)).tolist()

    for i in range(len(ypred)):
        res[i] = ypred[i]

    return jsonify(res)


@app.route('/api/prediction/DT/', methods=['POST'])
def prediction2():
    """

    Function run at each API call

    """

    """

    Function run at each API call

    """

    jsonfile = request.get_json()

    data = pd.read_json(json.dumps(jsonfile), orient='index', convert_dates=['dteday'])

    print(data)

    res = dict()

    modelfile = 'dr.pkl'
    model = pickle.load(open(modelfile, 'rb'))

    ypred = model.predict(parsedata(data)).tolist()

    for i in range(len(ypred)):
        res[i] = ypred[i]

    return jsonify(res)


@app.route('/api/prediction/XGB/', methods=['POST'])
def prediction3():
    """

    Function run at each API call

    """

    """

    Function run at each API call

    """

    jsonfile = request.get_json()

    data = pd.read_json(json.dumps(jsonfile), orient='index', convert_dates=['dteday'])

    print(data)

    res = dict()

    modelfile = 'xgb.pkl'
    model = pickle.load(open(modelfile, 'rb'))

    ypred = model.predict(parsedata(data)).tolist()

    for i in range(len(ypred)):
        res[i] = ypred[i]

    return jsonify(res)


if __name__ == '__main__':

    print("loaded OK")

    app.run(debug=True)
