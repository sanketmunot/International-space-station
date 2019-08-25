import requests
import turtle
import time
screen = turtle.Screen()
screen.setup(1240, 620)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.penup()
flag = True
try:
    while flag:
        url = requests.get("http://api.open-notify.org/iss-now.json")
        data = url.json()
        lat = float(data['iss_position']['latitude'])
        long = float(data['iss_position']['longitude'])
        iss.goto(long, lat)
except:
    flag = False
    screen._destroy()
finally:
    exit()