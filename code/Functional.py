from typing import Callable, List
import sensor_bindings
import actuator_bindings
import time

SCD4X_address = 0x62
VEML6030_address = 0x48

HUMIDITY_HIGH = 65
HUMIDITY_HIGH_THRESHOLD = 60
HUMIDITY_LOW = 45
HUMIDITY_LOW_THRESHOLD = 50
BRIGHTNESS_HIGH = 700
BRIGHTNESS_LOW = 300

#sensoren declaratie
humidity_sensor = sensor_bindings.SCD4X(SCD4X_address)
light_sensor = sensor_bindings.VEML6030(VEML6030_address)

#actuatoren declaratie
Fan = actuator_bindings.Fan()
Humidifier = actuator_bindings.Humidifier()
Light = actuator_bindings.Light()

def humidity_control(scd4x_sensor, fan_actuator, humidifier_actuator):
    humidity = scd4x_sensor.readHumidity()

    if humidity > HUMIDITY_HIGH:
        fan_actuator.startFan()
    elif humidity < HUMIDITY_HIGH_THRESHOLD:
        fan_actuator.stopFan()

    if humidity < HUMIDITY_LOW:
        humidifier_actuator.turnHumidifierOn()
    elif humidity > HUMIDITY_LOW_THRESHOLD:
        humidifier_actuator.turnHumidifierOff()

def light_control(veml6030_sensor, light_actuator):
    brightness = veml6030_sensor.readBrightness()

    if brightness < BRIGHTNESS_LOW:
        light_actuator.turnLightOn()
    elif brightness > BRIGHTNESS_HIGH:
        light_actuator.turnLightOff()

#Opzet van de pure functies om te vergelijken of de lezing binnen een bepaalde threshold is.
def checkThreshold(reading, threshold, high=True):
    if high:
        return reading > threshold
    else: 
        return reading < threshold

#opzet voor de hogere orde functie.
def controller(read_func: Callable, action_func: Callable, threshold: float, condition_func: Callable) -> None:
    try:
        reading = read_func()
        should_act = condition_func(reading, threshold)
        if should_act:
            action_func()
            return True
    except Exception as e:
        print(f"Error in controller functino: {e}")
    return False

#uitvoering van functie compositie van onderaan het bestand.
def test_actuatoren(*actions: List[Callable]) -> Callable:
    def execute_test():
        for action in actions:
            action()
    return execute_test

#controller logika met gebruik van hogere orde functies.
def controlEnvironment():
    humidity = humidity_sensor.readHumidity()
    brightness = light_sensor.readBrightness()

    if humidity > HUMIDITY_HIGH:
        controller(
            lambda: humidity,
            Fan.startFan,
            HUMIDITY_HIGH,
            lambda x, y: x > y
        )
    elif humidity < HUMIDITY_LOW:
        controller(
            lambda: humidity,
            Humidifier.turnHumidifierOn,
            HUMIDITY_LOW,
            lambda x, y: x < y
        )
    elif humidity > HUMIDITY_LOW_THRESHOLD:
        controller(
            lambda: humidity,
            Humidifier.turnHumidifierOff,
            HUMIDITY_LOW_THRESHOLD,
            lambda x, y: x > y
        )
    elif humidity < HUMIDITY_HIGH_THRESHOLD:
        controller(
            lambda: humidity,
            Fan.stopFan,
            HUMIDITY_HIGH_THRESHOLD,
            lambda x, y: x < y
        )

    if brightness < BRIGHTNESS_LOW:
        controller(
            lambda: brightness,
            Light.turnLightOn,
            BRIGHTNESS_LOW,
            lambda x, y: x < y
        )
    elif brightness > BRIGHTNESS_HIGH:
        controller(
            lambda: brightness,     
            Light.turnLightOff,
            BRIGHTNESS_HIGH,
            lambda x, y: x > y
        )

def test_loop():
    while True:
        controlEnvironment()
        time.sleep(1)