import os
import commands
import unittest
from lettuce import Runner

class LettuceTest(unittest.TestCase):
    def test_something(self):
        self.assertEquals(10,10)

class LettuceTestSuite(unittest.TestSuite):
    def suite(self):
        return suite()
    
def test_generator(feature):
    print "Received "+feature
    def test(self):
        print "Running lettuce on "+feature
        runner = Runner(feature,scenarios=None,verbosity=0,enable_xunit=True)
        result = runner.run()
        if (result.feature_results[0].passed==True):
            self.assertTrue(True)
        else:
            #Find out what failed
            msg = ""
            for scenario_result in result.feature_results[0].scenario_results:
                if (scenario_result.passed == False):
                    scenario = scenario_result.scenario
                    msg += "\nScenario '%s' failed" % scenario.name
                    for step in scenario.steps:
                        if (step.failed == True):
                            msg+= "\n\tStep '%s' failed" % step.original_sentence
                            msg+= "\n\t\tCause: %s" % step.why.cause
                            msg+= "\n\t\tException: %s" % step.why.exception
                            msg+= "\n\t\tTraceback: %s" % step.why.traceback
            self.fail(msg)
    return test

def suite():
    testFolder = os.path.dirname(__file__)
    featuresFolder = os.path.join(testFolder,"features")
    print "Starting run in "+featuresFolder
    listing = os.listdir(featuresFolder)
    for feature in listing:
        ext = os.path.splitext(feature)[1]
        if (ext == '.feature'):
            name = "test: "+feature
            feature = featuresFolder+"/"+feature
            print "Creating "+name+" using "+feature
            test = test_generator(feature)
            setattr(LettuceTest,name,test)
    print "Starting test run"
    suite = unittest.TestLoader().loadTestsFromTestCase(LettuceTest)
    return suite
    
def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
