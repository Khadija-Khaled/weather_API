from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])

def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'cairo'

    key = "da664cacef5c8ee85ae34cda8ce722fb"

    url = "http://api.openweathermap.org/data/2.5/weather?"

    params = {
    "APPID" : key,
    "q":city,
    "units": "metric"

    }
    res = requests.get(url, params=params)
    res = json.loads(res.text)
    #print(res)
    data = { 
            "country_code": str(res['sys']['country']), 
            "city_name": str(res['name']),
            "temp": str(res['main']['temp']) + ' C', 
            "pressure": str(res['main']['pressure']) + " hPa", 
            "humidity": str(res['main']['humidity']) + "%",
            "wind": str(res['wind']['speed']) + ' m/s'
    } 
    print(data) 
    return render_template('index.html', data = data) 

if __name__ == '__main__': 
    app.run(debug = True) #debug = true, allows the server to reload itself when changes are made


