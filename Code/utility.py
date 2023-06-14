import datetime
import requests


def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def current_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")

def weather(city):
    pass
