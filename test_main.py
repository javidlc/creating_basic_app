import unittest
from main import get_rate

class TestGetrate(unittest.TestCase):
    def test_get_rate(self):
        """
        Check if the get_rate function return a string as output
        Check if the get_rate function return the expected outcomes
        """
        # => To be filled by student
        #check: get_rate

        #string output
        self.assertEqual(type(get_rate("EUR","AUD")), str)
        #not valid arguments 
        self.assertEqual(get_rate("EEE","AUD"),"EEE is not a valid option. Please type another one.")
        self.assertEqual(get_rate("EUR","AAA"),"AAA is not a valid option. Please type another one.")
        self.assertEqual(get_rate("EEE","AAA"),"EEE and AAA are not valid options. Please type other ones.")
