def humidity_control(scd4x_sensor, fan_actuator, humidifier_actuator):
    humidity = scd4x_sensor.readHumidity()

    if humidity > 65:
        fan_actuator.startFan()
    elif humidity < 60:
        fan_actuator.stopFan()

    if humidity < 45:
        humidifier_actuator.turnHumidifierOn()
    elif humidity > 50:
        humidifier_actuator.turnHumidifierOff()

def light_control(veml6030_sensor, light_actuator):
    brightness = veml6030_sensor.readBrightness()

    if brightness < 100:
        light_actuator.turnLightOn()
    elif brightness > 500:
        light_actuator.turnLightOff()