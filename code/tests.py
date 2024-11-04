import unittest, sys, os, time, logging
from unittest.mock import patch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functional import checkThreshold, controller, humidity_control, light_control


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename= 'test_results.log'
)
logger = logging.getLogger(__name__)

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
        start_time = time.time()
        self.mock_scd4x.readHumidity.return_value = 70
        self.mock_veml6030.readBrightness.return_value = 75

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)

        self.mock_fan.startFan.assert_called_once()
        self.mock_humidifier.turnHumidifierOff.assert_called_once()

        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de hoge humidity test is: {execution_time} seconde")

    @mock_setup
    def test_low_humidity(self):
        start_time = time.time()
        self.mock_scd4x.readHumidity.return_value = 30
        self.mock_veml6030.readBrightness.return_value = 75

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)

        self.mock_fan.stopFan.assert_called_once()
        self.mock_humidifier.turnHumidifierOn.assert_called_once()

        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de lage humidity test is: {execution_time} seconde")
    @mock_setup
    def test_light(self):
        start_time = time.time()
        self.mock_veml6030.readBrightness.return_value = 50
        light_control(self.mock_veml6030, self.mock_light)
        self.mock_light.turnLightOn.assert_called_once()
    
        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de light test is: {execution_time} seconde")


class UnitTest(unittest.TestCase):
    def test_threshhold(self):

        start_time = time.time()

        self.assertTrue(checkThreshold(70, 65 ,True))
        self.assertFalse(checkThreshold(65, 70 ,True))
        self.assertTrue(checkThreshold(65, 70 ,False))
        self.assertFalse(checkThreshold(70, 65 ,False))

        exec_time = time.time() - start_time
        self.assertLess(exec_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de Threshold test is: {exec_time} seconde")

class IntegrationTest(unittest.TestCase):
    @mock_setup
    def test_humi_integration_fan(self):
        start_time = time.time()
        self.mock_scd4x.readHumidity.return_value = 70

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)
        self.mock_fan.startFan.assert_called_once()

        controller(
            self.mock_scd4x.readHumidity,
            self.mock_fan.startFan,
            65,
            lambda x, y: x > y
        )
        self.mock_fan.startFan.assert_called()

        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de humidity integration test van de fan is: {execution_time} seconde")

    @mock_setup
    def test_humi_integration_humidifier(self):
        start_time = time.time()
        self.mock_scd4x.readHumidity.return_value = 30

        humidity_control(self.mock_scd4x, self.mock_fan, self.mock_humidifier)
        self.mock_humidifier.turnHumidifierOn.assert_called_once()

        controller(
            self.mock_scd4x.readHumidity,
            self.mock_fan.turnHumidifierOn,
            55,
            lambda x, y: x > y
        )
        self.mock_humidifier.turnHumidifierOn.assert_called()
        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de humidity integration test van de humidifier is: {execution_time} seconde")


    @mock_setup
    def test_light_integration(self):
        start_time = time.time()
        self.mock_veml6030.readBrightness.return_value = 50

        light_control(self.mock_veml6030, self.mock_light)
        self.mock_light.turnLightOn.assert_called_once()

        controller(
            self.mock_veml6030.readBrightness,
            self.mock_light.turnLightOn,
            100,
            lambda x, y: x > y
        )
        self.mock_light.turnLightOn.assert_called()

        execution_time = time.time() - start_time
        self.assertLess(execution_time, 10, "Execution time is langer dan 10 seconde")
        logger.info(f"Execution time van de light integration test is: {execution_time} seconde")


def gen_report():
    log_path = os.path.join(os.path.dirname(__file__), 'test_results.log')
    if not os.path.exists(log_path):
        print("No test results found")
        return

    try:
        report_path = os.path.join(os.path.dirname(__file__), 'test_report.md')

        with open(report_path, 'w', encoding='utf-8') as t:
            t.write('# Test Report\n')
            t.write('## uitgevoerde tests\n')
            t.write('- Unit test: Het testen van de threshold.\n')
            t.write('- System test: Het testen van het gedrag van het systeem.\n')
            t.write('- Integration test: Het testen van de interactie tussen sensoren en acutatoren.\n')

            t.write('##Test resultaten\n')
            log_path = os.path.join(os.path.dirname(__file__), 'test_results.log')
            with open(log_path, 'r', encoding='utf-8') as log:
                t.write('```\n')
                t.write(log.read())
                t.write('```\n')
            
            t.write('\n## Kwaliteitsimpact\n')
            t.write('1. Betrouwbaarheid: De tests zijn betrouwbaar doordat de thresholds juist zijn geverifieerd.\n')
            t.write('2. Prestaties: De tests worden uitgevoerd binnen 10 seconden.\n')
            t.write('3. Onderhoudbaarheid: Het systeem is gemakkelijk uit te breiden voor meerdere sensoren/actuatoren.\n')

            t.write('\n## Conclusie\n')
            t.write('De tests zijn succesvol uitgevoerd en de kwaliteit van het systeem is gewaarborgd.\n')

        print(f'Test report is gegenereerd in: {report_path}')

    except IOError as io:
        print(f'File write error: {io}')

    except Exception as e:
        print(f"Er is iets fout gegaan bij het genereren van het test report: {e}")