import unittest
from unittest.mock import patch, MagicMock
from decorators import read_SCD4X, read_VEML6030

class TestSensoren(unittest.TestCase):
    def test_read_scd4x(self):
        mock_scd4x = MagicMock()
        mock_scd4x.readHumidity.return_value = 50
        self.assertAlmostEqual(read_SCD4X(), 50)

    def test_read_VEML6030(self):
        mock_veml6030 = MagicMock()
        mock_veml6030.readBrightness.return_value = 400
        self.assertAlmostEqual(read_VEML6030(), 400)

if __name__ == '__main__':
    unittest.main()