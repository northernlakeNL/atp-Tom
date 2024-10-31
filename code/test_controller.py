import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller import humidity_control, light_control
from functional import checkThreshold, controller, controlEnvironment, SCD4X_address, VEML6030_address


def mock_setup(func):
    """"decorator opzet voor alle benodigde mocks"""
    @patch('sensor_bindings.SCD4X')
    @patch('sensor_bindings.VEML6030')
    @patch('actuator_bindings.Fan')
    @patch('actuator_bindings.Humidifier')
    @patch('actuator_bindings.Light')
    def wrapper(self, MockLight, MockHumidifier, MockFan, MockVEML6030, MockSCD4X, *agrs, **kwargs):
        self.mock_scd4x = MockSCD4X.return_value
        self.mock_veml6030 = MockVEML6030.return_value
        self.mock_fan = MockFan.return_value
        self.mock_humidifier = MockHumidifier.return_value
        self.mock_light = MockLight.return_value
        return func(self, *agrs, **kwargs)
    return wrapper

class SystemTest(unittest.TestCase):
    """System tests voor control system"""
    @mock_setup
    def test_high_humidity(self):
        self.mock_scd4x.readHumidity.return_value = 70
        self.mock_veml6030.readBrightness.return_value = 75

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)

        self.mock_fan.startFan.assert_called_once()
        self.mock_humidifier.turnHumidifierOff.assert_called_once()

    @mock_setup
    def test_low_humidity(self):
        self.mock_scd4x.readHumidity.return_value = 30
        self.mock_veml6030.readBrightness.return_value = 75

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)

        self.mock_fan.stopFan.assert_called_once()
        self.mock_humidifier.turnHumidifierOn.assert_called_once()

    @mock_setup
    def test_light(self):
        self.mock_veml6030.readBrightness.return_value = 50
        light_control(self.mock_veml6030, self.mock_light)
        self.mock_light.turnLightOn.assert_called_once()

class UnitTest(unittest.TestCase):
    def test_threshhold(self):
        self.assertTrue(checkThreshold(70, 65 ,True))
        self.assertFalse(checkThreshold(65, 70 ,True))
        self.assertTrue(checkThreshold(65, 70 ,False))
        self.assertFalse(checkThreshold(70, 65 ,False))

class IntegrationTest(unittest.TestCase):
    @patch('sensor_bindings.SCD4X')
    def test_sensor_actuator(self, MockSCD4X):
        mock_scd4x = MockSCD4X.return_value
        mock_scd4x.readHumidity.return_value = 70
        mock_action = MagicMock()

        result = controller(
            mock_scd4x.readHumidity,
            mock_action,
            65,
            lambda x, y : x > y
        )
        self.assertTrue(result)
        mock_action.assert_called_once()

# class test_controller(unittest.TestCase):
#     def test_controller_humidity_high(self):
#         mock_scd4x = MagicMock()
#         mock_fan = MagicMock()
#         mock_humidifier = MagicMock()

#         mock_scd4x.readHumidity.return_value = 70
#         humidity_control(mock_scd4x, mock_fan, mock_humidifier)
#         mock_fan.startFan.assert_called_once()
        
#         mock_scd4x.readHumidity.return_value = 55
#         humidity_control(mock_scd4x, mock_fan, mock_humidifier)
#         mock_fan.stopFan.assert_called_once()

#     def test_controller_humidity_low(self):
#         mock_scd4x = MagicMock()
#         mock_fan = MagicMock()
#         mock_humidifier = MagicMock()

#         mock_scd4x.readHumidity.return_value = 30
#         humidity_control(mock_scd4x, mock_fan, mock_humidifier)
#         mock_humidifier.turnHumidifierOn.assert_called_once()
        
#         mock_scd4x.readHumidity.return_value = 55
#         humidity_control(mock_scd4x, mock_fan, mock_humidifier)
#         mock_humidifier.turnHumidifierOff.assert_called_once()

#     def test_controller_light(self):
#         mock_veml630 = MagicMock()
#         mock_light = MagicMock()
#         mock_veml630.readBrightness.return_value = 50
#         light_control(mock_veml630, mock_light)
#         mock_light.turnLightOn.assert_called_once()

#         mock_veml630.readBrightness.return_value = 600
#         light_control(mock_veml630, mock_light)
#         mock_light.turnLightOff.assert_called_once() 

if __name__ == '__main__':
    unittest.main()