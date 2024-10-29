import unittest
from unittest.mock import patch, MagicMock
from actuator_bindings import Fan, Humidifier, Light

class TestActuatoren(unittest.TestCase):
    def test_fan(self):
        mock_fan = MagicMock()
        mock_fan.startFan().assert_called_once()

        mock_fan.stopFan().assert_called_once()

    def test_humidifier(self):
        mock_humidifier = MagicMock()
        mock_humidifier.turnHumidifierOn().assert_called_once()
    
        mock_humidifier.turnHumidifierOff().assert_called_once()

    def test_light(self):
        mock_light = MagicMock()
        mock_light().turnLightOn().assert_called_once()
    
        mock_light().turnLightOff().assert_called_once()

if __name__ == '__main__':
    unittest.main()