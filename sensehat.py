from datetime import datetime


from sense_hat import SenseHat


def demo():
    now = datetime.now().strftime('%H:%M:%S')
    sense = SenseHat()
    sense.low_light=True
    sense.show_message("Hi ELON!", text_colour=[255,0,0], back_colour=[125,125,125])
    sense.show_message(now, scroll_speed=0.05)
    return 0