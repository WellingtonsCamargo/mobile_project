import os
import glob
import unittest
from time import sleep
from Elements import _element
from Objects import _object


class AndroidWebViewTests(unittest.TestCase):

    def test_Acessando_Pagina(self):
        _object.click_element_locator(_element.myGarden)
        _object.await_element_locator(_element.emptyGarden)
        _object.capturaPng('Energia/Home')
        _object.click_element_locator(_element.addPlanta)
        _object.validation_element_locator(_element.plantList,'PLANT LIS')
        _object.capturaPng('Energia/Plant_list')
        _object.tearDown()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    _object.tearDown()

# pytest main.py --html-report=./report/report.html