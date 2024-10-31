import unittest
from unittest.mock import patch, MagicMock
from decorators import read_SCD4X, read_VEML6030

class TestSensoren(unittest.TestCase):
    @patch('decorators.sensor_bindings.SCD4X')
    def test_read_scd4x(self, MockSCD4X):
        mock_scd4x = MockSCD4X.return_value
        mock_scd4x.readHumidity.return_value = 50
        self.assertEqual(read_SCD4X(), 50)

    @patch('decorators.sensor_bindings.VEML6030')
    def test_read_VEML6030(self, MockVEML6030):
        mock_veml6030 = MockVEML6030.return_value
        mock_veml6030.readBrightness.return_value = 400
        self.assertEqual(read_VEML6030(), 400)

    @patch('decorators.sensor_bindings.i2c')
    def test_i2c_mock(self, mock_i2c):
        mock_i2c.read.return_value
        mock_i2c.read.side_effect


if __name__ == '__main__':
    unittest.main()