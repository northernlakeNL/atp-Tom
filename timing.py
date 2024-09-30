import time
import sensor_bindings

def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"called function {func.__name__} with args: {args}, kwargs: {kwargs}.\nThe result is {result}.")
        return result
    return wrapper

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} duurde {end_time - start_time:.4f} seconde")
        return result
    return wrapper

@timing
@logging
def read_sc4x():
    co2_sensor = sensor_bindings.SCD4X()
    return co2_sensor.readCO2()

@timing
@logging
def read_veml6030():
    light_sensor = sensor_bindings.VEML6030()
    return light_sensor.readLightIntensity()

if __name__ == "__main__":
    co2_value = read_sc4x()
    print(f"CO2 niveau is: {co2_value}")

    light_value = read_veml6030()
    print(f"licht felheid is: {light_value}")