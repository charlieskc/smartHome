from sense_hat import SenseHat
from datetime import datetime
from time import sleep

import requests

#sleep(5)


#now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
now = datetime.now().strftime('%H:%M:%S')
sense = SenseHat()
sense.low_light=True
sense.show_message("Hi ELON!", text_colour=[255,0,0], back_colour=[125,125,125])
sense.show_message(now, scroll_speed=0.05)


humidity = sense.get_humidity()
sense.show_message("HUD%"+ str("%0.2f" % humidity), scroll_speed=0.05)

temp = sense.get_temperature()
sense.show_message("Temp."+ str("%0.2f" % temp), scroll_speed=0.05)

temp = sense.get_temperature_from_humidity()
print("Temperature: %s C" % temp)


data=dict(title='humidity=' + str("%0.2f" % humidity)+ '%\nTemperture='+ str("%0.2f" % temp), body='HUD%' + str("%0.2f" % humidity)+ '\nTemperture='+ str("%0.2f" % temp), type='note')
requests.post('https://api.pushbullet.com/v2/pushes', auth=('o.ZBNInHoENd94UjTsedyvn6O1QGml0tPA',''), data=data)





event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
sleep(0.1)
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
