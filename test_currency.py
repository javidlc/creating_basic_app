import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_function(self):
        """
        Change parameters in check_valid_currency() to try other tests and responses
        """
        # => To be filled by student
        #check: check_valid_currency

        self.assertEqual(check_valid_currency("AUD"), True)
        self.assertEqual(check_valid_currency("aud"), True)
        self.assertEqual(check_valid_currency("XXX"), False)
        self.assertEqual(check_valid_currency("AUDD"), False)

class TestExtractApi(unittest.TestCase):
        # => To be filled by student
        #check:extract_api_result,Currency class

    def setUp(self):
        """
        Change the attributes below to try other tests
        """
        self.amount = 1
        self.from_currency = 'USD'
        self.date = '18/08/2021'
        self.to_currency = 'AUD'
        self.rate = 0.3
        self.inverse_rate = 3.33333

    def test_api_dictionary(self):
        """
        Test if extract_api_result give the same results as the setup defined
        """
        #data created to test the API
        data = {'amount': self.amount, 
                'base': self.from_currency, 
                'date': self.date, 
                'rates': {self.to_currency: self.rate}}

        #result from the api
        result_test = extract_api_result(data)

        self.assertEqual(self.amount,result_test.amount)
        self.assertEqual(self.from_currency,result_test.from_currency)
        self.assertEqual(self.to_currency,result_test.to_currency)
        self.assertEqual(self.date,result_test.date)
        self.assertEqual(self.rate,result_test.rate)
        #check the inverse rate from Currency
        self.assertEqual(self.inverse_rate,result_test.inverse_rate)
        #check the final message from Currency
        self.assertEqual(f"Today's ({self.date}) conversion rate from {self.from_currency} to {self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}.", result_test.format_result())

    def test_api_none(self):
        """
        Expected to fail: extract_api_result needs a dictionary as input
        """

        #data created to test the API: None
        data = None

        #result from the api
        result_test = extract_api_result(data)

        self.assertEqual(None,result_test.amount)
        self.assertEqual(None,result_test.from_currency)
        self.assertEqual(None,result_test.to_currency)
        self.assertEqual(None,result_test.date)
        self.assertEqual(None,result_test.rate)
        self.assertEqual(None,result_test.inverse_rate)


    def test_api_text(self):
        """
        Expected to fail: extract_api_result needs a dictionary as input
        """

        #data created to test the API: text
        data = "text"

        #result from the api
        result_test = extract_api_result(data)

        self.assertEqual(None,result_test.amount)
        self.assertEqual(None,result_test.from_currency)
        self.assertEqual(None,result_test.to_currency)
        self.assertEqual(None,result_test.date)
        self.assertEqual(None,result_test.rate)
        self.assertEqual(None,result_test.inverse_rate)

    def test_api_empty(self):
        """
        Expected to fail: extract_api_result needs a dictionary as input 
        """

        #data created to test the API: empty dictionary
        data = {}

        #result from the api
        result_test = extract_api_result(data)

        self.assertEqual(None,result_test.amount)
        self.assertEqual(None,result_test.from_currency)
        self.assertEqual(None,result_test.to_currency)
        self.assertEqual(None,result_test.date)
        self.assertEqual(None,result_test.rate)
        self.assertEqual(None,result_test.inverse_rate)

    def test_currency_class(self):
        """"
        Test if a object created is class Currency
        """
        #create object
        currency= Currency()
        self.assertEqual(isinstance(currency, Currency), True)
        

    def test_api_currency_equal(self):
        """
        Test if extract_api_result give the same results as a Currency class 
        created separatedly with same inputs.
        """
        #data created to test the API
        data = {'amount': self.amount, 
                'base': self.from_currency, 
                'date': self.date, 
                'rates': {self.to_currency: self.rate}}

        #Currency created to test:
        currency = Currency(amount = self.amount, 
                            from_currency = self.from_currency,
                            date = self.date,
                            to_currency = self.to_currency,
                            rate = self.rate)
        #get the inverse_rate:
        currency.reverse_rate()

        #result from the api
        result_test = extract_api_result(data)

        self.assertEqual(currency.amount,result_test.amount)
        self.assertEqual(currency.from_currency,result_test.from_currency)
        self.assertEqual(currency.to_currency,result_test.to_currency)
        self.assertEqual(currency.date,result_test.date)
        self.assertEqual(currency.rate,result_test.rate)
        self.assertEqual(currency.inverse_rate,result_test.inverse_rate)

