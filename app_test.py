import requests, json

if __name__ == '__main__':
    singledatapoint = json.dumps({"0": {"datetime": "2011-07-01 10:00:00", "season": 3,
                             "holiday": 1, "workingday": 0, "weather": 4, "temp": 0.23,
                             "atemp": 0.19, "humidity": 0.2, "windspeed": 0.5}})

    multidatapoints = json.dumps({"0": {"datetime": "2011-01-01 10:00:00", "season": 1,
                             "holiday": 0, "workingday": 0, "weather": 2, "temp": 0.167,
                             "atemp": 0.18, "humidity": 0.67, "windspeed": 0.17},
                       "1": {"datetime": "2012-01-01 10:00:00", "season": 2,
                             "holiday": 1, "workingday": 0, "weather": 1, "temp": 0.212,
                             "atemp": 0.234, "humidity": 0.82, "windspeed": 0.02},
                       "2": {"datetime": "2011-04-01 17:00:00", "season": 4,
                             "holiday": 0, "workingday": 0, "weather": 3, "temp": 0.34,
                             "atemp": 0.36, "humidity": 0.2, "windspeed": 0.1}
                       })

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

    url = "http://127.0.0.1:5000/api/prediction/LM/"
    r = requests.post(url, data=singledatapoint, headers=headers)
    print(r, r.text)

    url = "http://127.0.0.1:5000/api/prediction/DT/"
    r = requests.post(url, data=singledatapoint, headers=headers)
    print(r, r.text)

    url = "http://127.0.0.1:5000/api/prediction/LM/"
    r = requests.post(url, data=multidatapoints, headers=headers)
    print(r, r.text)

    url = "http://127.0.0.1:5000/api/prediction/DT/"
    r = requests.post(url, data=multidatapoints, headers=headers)
    print(r, r.text)

    url = "http://127.0.0.1:5000/api/prediction/XGB/"
    r = requests.post(url, data=multidatapoints, headers=headers)
    print(r, r.text)
