import unittest
from unittest.mock import patch, MagicMock
from controller import humidity_control, light_control

class test_controller(unittest.TestCase):
    def test_controller_humidity_high(self):
        mock_scd4x = MagicMock()
        mock_fan = MagicMock()
        mock_humidifier = MagicMock()

        mock_scd4x.readHumidity.return_value = 70
        humidity_control(mock_scd4x, mock_fan, mock_humidifier)
        mock_fan.startFan.assert_called_once()
        
        mock_scd4x.readHumidity.return_value = 55
        humidity_control(mock_scd4x, mock_fan, mock_humidifier)
        mock_fan.stopFan.assert_called_once()

    def test_controller_humidity_low(self):
        mock_scd4x = MagicMock()
        mock_fan = MagicMock()
        mock_humidifier = MagicMock()

        mock_scd4x.readHumidity.return_value = 30
        humidity_control(mock_scd4x, mock_fan, mock_humidifier)
        mock_humidifier.turnHumidifierOn.assert_called_once()
        
        mock_scd4x.readHumidity.return_value = 55
        humidity_control(mock_scd4x, mock_fan, mock_humidifier)
        mock_humidifier.turnHumidifierOff.assert_called_once()

    def test_controller_light(self):
        mock_veml630 = MagicMock()
        mock_light = MagicMock()
        mock_veml630.readBrightness.return_value = 50
        light_control(mock_veml630, mock_light)
        mock_light.turnLightOn.assert_called_once()

        mock_veml630.readBrightness.return_value = 600
        light_control(mock_veml630, mock_light)
        mock_light.turnLightOff.assert_called_once() 

if __name__ == '__main__':
    unittest.main()