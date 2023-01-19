from flask import Flask
from flask import render_template
from flask import request
import requests
import json

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/check_weather')
def check_weather():
    return render_template('home.html')

@app.route('/check_weather_result')
def check_weather_result():
    city = request.args.get('city')
    temperature = get_weather_data(city)
    return render_template('result.html', city = city, temperature = temperature)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&limit=1&appid=6965d9741d40b5b0ee40d819d75dbced"
    response = requests.request("GET", url)
    json_obj = json.loads(response.text)
    temp_in_kelvin = json_obj["main"]["temp"]
    temp_in_celcius = temp_in_kelvin - 273.15
    round_temp_in_celcius = round(temp_in_celcius, 2)
    return round_temp_in_celcius




if __name__ == '__main__':
      app.run()
