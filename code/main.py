import unittest
import time
from tests import SystemTest, UnitTest, IntegrationTest, gen_report
from sim import EnvironmentSim

def run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(SystemTest))
    suite.addTests(loader.loadTestsFromTestCase(UnitTest))
    suite.addTests(loader.loadTestsFromTestCase(IntegrationTest))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    gen_report()

    return result.wasSuccessful()

if __name__ == '__main__':
    # uitvoeren van de tests
    run_tests()
    # wachten voor de simulatie
    time.sleep(10)
    # uitvoeren van de simulatie
    EnvironmentSim().simulate()