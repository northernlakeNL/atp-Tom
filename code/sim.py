import time
import random
from rich.console import Console
from rich.table import Table
from functional import controlEnvironment, humidity_control, light_control
import sensor_bindings
import actuator_bindings

SCD4X_address = 0x62
VEML6030_address = 0x48

humidity_sensor = sensor_bindings.SCD4X(SCD4X_address)
light_sensor = sensor_bindings.VEML6030(VEML6030_address)
Fan = actuator_bindings.Fan()
Humidifier = actuator_bindings.Humidifier()
Light = actuator_bindings.Light()

class EnvironmentSim:
    def __init__(self):
        self.console = Console()
        self.humidity = humidity_sensor.readHumidity()
        self.brightness = light_sensor.readBrightness()
        self.limits = {
            'humidity': (25, 75),
            'brightness': (100, 1000)
        }

    def values_update(self):
        new_humidity = max(self.limits['humidity'][0],
                            min(self.limits['humidity'][1],
                            self.humidity + random.uniform(-10, 10)
                        ))
        humidity_sensor.setSimulatedHumidity(new_humidity)
        self.humidity = new_humidity
        new_brightness = max(self.limits['brightness'][0],
                            min(self.limits['brightness'][1],
                            self.brightness + random.uniform(-100, 100)
                        ))
        light_sensor.setSimulatedBrightness(new_brightness)
        self.brightness = new_brightness

    def display(self):
        table1 = Table(title="Environment Simulation")
        table1.add_column("Sensor", style="cyan")
        table1.add_column("Value", style="magenta")
        table1.add_row("Humidity", f"{self.humidity:.1f}%")
        table1.add_section()
        table1.add_row("Brightness", f"{self.brightness:.1f} lux")

        table2 = Table(title="Control System")
        table2.add_column("Actuator", style="cyan")
        table2.add_column("Status", style="magenta")
        table2.add_row("Fan", 'ON' if Fan.getState() else 'OFF')
        table2.add_section()
        table2.add_row("Humidifier", 'ON' if Humidifier.getState() else 'OFF')
        table2.add_section()
        table2.add_row("Light", 'ON' if Light.getState() else 'OFF')
        self.console.clear()
        self.console.print(table1)
        self.console.print(table2)

    def get_states(self):
        return {
            'Fan': Fan.getState(),
            'Humidifier': Humidifier.getState(),
            'Light': Light.getState()
        }

    def simulate(self):
        try:
            while True:
                self.display()
                humidity_sensor.setSimulatedHumidity(self.humidity)
                light_sensor.setSimulatedBrightness(self.brightness)
                humidity_control(humidity_sensor, Fan, Humidifier)
                light_control(light_sensor, Light)
                self.get_states()
                controlEnvironment()

                self.values_update()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nSimulation stopped")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    sim = EnvironmentSim()
    sim.simulate()  