from typing import Callable
import sensor_bindings
import actuator_bindings
import time

SCD4X_address = 0x62
VEML6030_address = 0x48

#sensoren declaratie
humidity_sensor = sensor_bindings.SCD4X(SCD4X_address)
light_sensor = sensor_bindings.VEML6030(VEML6030_address)

Fan = actuator_bindings.Fan()
Humidifier = actuator_bindings.Humidifier()
Light = actuator_bindings.Light()

#actuatoren declaratie
Fan.startFan()
Fan.stopFan()

Humidifier.turnHumidifierOn()
Humidifier.turnHumidifierOff()

Light.turnLightOn()
Light.turnLightOff()

#Opzet van de pure functies om te vergelijken of de lezing binnen een bepaalde threshold is.
def checkThreshold(reading, threshold, high=True):
    if high:
        return reading > threshold
    else: 
        return reading < threshold

#opzet voor de hogere orde functie.
def controller(read_func: Callable, action_func: Callable, threshold: float, condition_func: Callable) -> None:
    reading = read_func()
    if condition_func(reading, threshold):
        action_func()
        return True
    return False

#uitvoering van functie compositie van onderaan het bestand.
def test_actuatoren(*actions):
    def execute_test():
        for action in actions:
            action()
    return execute_test

#controller logika met gebruik van hogere orde functies.
def controlEnvironment():
    humidity = humidity_sensor.readHumidity()
    brightness = light_sensor.readBrightness()

    controller(
        lambda: humidity,
        Humidifier.turnHumidifierOn if humidity < 45 else Humidifier.turnHumidifierOff if humidity > 50 else None,
        45,
        lambda x, y: x > y
    )
    controller(
        lambda: humidity,
        Fan.startFan if humidity > 65 else Fan.fanStop if humidity < 55 else None,
        65,
        Fan.startFan,
        lambda reading: checkThreshold(reading, 65, high=False)
    )
    controller(
        lambda: brightness,
        Light.turnLightOn if brightness < 50 else Light.turnLightOff if brightness > 100 else None,
        50,
        lambda x, y: x > y
    )

def test_loop():
    while True:
        controlEnvironment()
        time.sleep(1)