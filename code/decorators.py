import time
from functools import wraps
import sensor_bindings

def MeasurementConverter(func):
    """
    Een decorator voor het omzetten van een Celsius-waarde in Fahrenheit.
    :param func: De functie die een Celsius-waarde moet omzetten.
    :return: een gewrapte functie met een omgezette waarden van Celsius in Fahrenheit.
    """
    @wraps(func)
    def MC_wrapper(*args, **kwargs):
        """
        Een wrapper voor het omzetten van een Celsius-waarde in Fahrenheit.
        :param args: De argumenten van de functie.
        :param kwargs: De keyword argumenten van de functie.
        :return: Het resultaat van de functie, omgezet in Fahrenheit.
        """
        celcius_value = func(*args, **kwargs)
        farenheit_value = (celcius_value *9/5) + 32
        return farenheit_value
    return MC_wrapper

def caching(func):
    """
    Een decorator voor het cachen van de resultaten van een functie.

    De decorator zorgt ervoor dat de resultaten van een functie opgeslagen en gecached kunnen worden,
    zodat als dezelfde argumenten met de functie worden meegegeven, de gecachede resultaten teruggegeven.

    :param func: De functie die gecached moet worden.
    :return: een gewrapte functie met de caching.
    """
    cache = {}
    @wraps(func)
    def cache_wrapper(*args):
        """
        Een wrapper voor het cachen van de resultaten.

        :param args: De argumenten van de functie.

        :return: Het resultaat van de functie, of het gecached resultaat.
        """
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return cache_wrapper

def logging(func):
    """
    Een decorator voor het loggen van een functie.

    De decorator voegt een loggingsfunctie toe aan een bestaande functie.
    Het registreerd de naam, de argumenten en het resultaat van de functie.

    :param func: De functie die gelogd moet worden.
    :return: een gewrapte functie met de log.
    """
    @wraps(func)
    def log_wrapper(*args, **kwargs):
        """
        Een wrapper voor de loggingsfunctie.

        De wrapper zorgt ervoor dat de functie naam, de argumenten en het resultaat van de functie daadwerkelijk gelogd worden.

        :param args: De argumenten van de functie.
        :param kwargs: De keyword argumenten van de functie.
        :return: Het resultaat van de functie.
        """
        result = func(*args, **kwargs)
        print(f"called function {func.__name__} with args: {args}, kwargs: {kwargs}.\nThe result is {result}.")
        return result
    return log_wrapper

def timing(func):
    """
    Een decorator voor het meten van de tijd die een functie nodig heeft.
    
    De decorator zorgt ervoor dat de tijd dat de functie nodig heeft om te runnen gelogd wordt.
    
    :param func: De functie die gemeten moet worden.
    :return: een gewrapte functie met de timing.
    """
    @wraps(func)
    def time_wrapper(*args, **kwargs):
        """
        Een wrapper voor het meten van de tijd.
        
        De wrapper meet de tijd die de functie nodig heeft om te runnen.
        
        :param args: De argumenten van de functie.
        :param kwargs: De keyword argumenten van de functie.
        :return: Het resultaat van de functie.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} duurde {end_time - start_time:.4f} seconde")
        return result
    return time_wrapper

@timing
@logging
@caching
def read_SCD4X():
    """
    Leest het luchtvochtigheids niveau uit de SCD4X sensor.

    :return: de gemeete waarden van readCO2.
    """
    humidity_sensor = sensor_bindings.SCD4X()
    return humidity_sensor.readHumidity()

@timing
@logging
@caching
def read_VEML6030():
    """
    Leest het lichtintensity uit de VEML6030 sensor.

    :return: de gemeente waarden van readLightIntensity.
    """
    light_sensor = sensor_bindings.VEML6030()
    return light_sensor.readBrightness()
