#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import requests
import json

API_KEY = 'a5b74bcd1a10b3ee324a0bf25c1b247d'


def get_geo_by_ip():

    ip = requests.get('https://api.ipify.org').text
    send_url = "http://api.ipstack.com/{}?access_key=c755c7cae07cf8943a551ee0562b3825".format(ip)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']

    return latitude, longitude


def get_weather_by_geo(API_KEY, lat, lon):

    url = "http://api.openweathermap.org/data/2.5/forecast?appid={}&lat={}&lon={}&units=metric".format(API_KEY, lat, lon)
    r = requests.get(url)

    response_list = r.json()
    city = response_list['city']['name']
    country = response_list['city']['country']
    temp = response_list['list'][0]['main']['temp']

    temp = int(temp)

    print('The weather in {}, {} is {} degrees'.format(city, country, temp))


def main():

    lat, lon = get_geo_by_ip()
    get_weather_by_geo(API_KEY, lat, lon)


if __name__ == '__main__':
    main()
