from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
while True:
    if ts.is_pressed():
        print("Pressed")
    else:
        pass