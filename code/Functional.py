import sensor_bindings

#sensoren declaratie
humidity_sensor = sensor_bindings.SCD4X()
light_sensor = sensor_bindings.VEML6030()

Fan = sensor_bindings.Fan()
Humidifier = sensor_bindings.Humidifier()
Light = sensor_bindings.Light()

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
def controller(read_func, action_func, threshold, condition_func):
    reading = read_func()
    if condition_func(reading, threshold):
        action_func()

#uitvoering van functie compositie van onderaan het bestand.
def test_actuatoren(*actions):
    def test_actuatoren():
        for action in actions:
            action()
    return test_actuatoren

#controller logika met gebruik van hogere orde functies.
def controlEnvironment():
    controller(
        humidity_sensor.readHumidity(),
        45,
        Humidifier.turnHumidifierOn,
        lambda reading: checkThreshold(reading, 45, high=False)
    )
    controller(
        humidity_sensor.readHumidity(),
        50,
        Humidifier.turnHumidifierOff,
        lambda reading: checkThreshold(reading, 50, high=True)
    )
    controller(
        humidity_sensor.readHumidity(),
        65,
        Fan.startFan,
        lambda reading: checkThreshold(reading, 65, high=False)
    )
    controller(
        humidity_sensor.readHumidity(),
        60,
        Fan.startFan,
        lambda reading: checkThreshold(reading, 60, high=False)
    )

    controller(
        light_sensor.readLightIntensity(),
        10000,
        Light.turnLightOn,
        lambda reading: checkThreshold(reading, 10000, high=True)
    )
    controller(
        light_sensor.readLightIntensity(),
        10000,
        Light.turnLightOff,
        lambda reading: checkThreshold(reading, 10000, high=True)
    )

#compositie van functies om actuatoren te gelijk aan of uit te kunnen zetten.
test_uit_acties = test_actuatoren(
    Humidifier.turnHumidifierOff,
    Fan.stopFan,
    Light.turnLightOff
)

test_aan_acties = test_actuatoren(
    Humidifier.turnHumidifierOn,
    Fan.startFan,
    Light.turnLightOn
)

#testen van de actuatoren

test_aan_acties()
test_uit_acties()
controlEnvironment()