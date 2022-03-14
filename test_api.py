import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_function(self):
        """
        Check if the return is ok and if they are strings
        """
        # => To be filled by student
        #check: format_currencies_url,format_latest_url
        self.assertEqual(format_currencies_url(), _HOST_ + _CURRENCIES_)
        self.assertEqual(format_latest_url("AUD","USD"), _HOST_ + _LATEST_+ '?from=' + "AUD" + '&to=' + "USD")
        self.assertEqual(isinstance(format_latest_url("AUD","USD"), str), True)
        self.assertEqual(isinstance(format_currencies_url(), str), True)


class TestAPI(unittest.TestCase):
    #check:call_api, get_currencies
    def test_api_call(self):
        """
        Check if the call_api is a request model response:
            for currency
            for latest
            for one bad request
        Check if the url is correct for the currencies code availables
        """
        # => To be filled by student
        url= _HOST_ + _CURRENCIES_
        url1= _HOST_ + _LATEST_
        url2 = _HOST_ + _CURRENCIES_ + _LATEST_

        #check if the return of call_api with currency is a request.models.response
        self.assertEqual(str(type(call_api(url))), str("<class 'requests.models.Response'>"))

        #check if the return of call_api with latest is a request.models.response
        self.assertEqual(str(type(call_api(url1))), str("<class 'requests.models.Response'>"))

        #check if a correct url has status code =200 (get_rate extract api result)
        self.assertEqual(call_api(url1).status_code ==200 , True)

        #check if an incorrect url still be a request models response
        self.assertEqual(str(type(call_api(url2))), str("<class 'requests.models.Response'>"))

        #check if an incorrect url has status code !=200 (error handle in get_rate function)
        self.assertEqual(call_api(url2).status_code !=200 , True)

        #check if the url is ok
        self.assertEqual(call_api(url).url, _HOST_ + _CURRENCIES_)

        #check if the url is ok
        self.assertEqual(call_api(url1).url, _HOST_ + _LATEST_)


    def test_get_currencies(self):
        """
        Check if get_currencies return a list.
        Check if that list is the same as the frankfurter.app: IMPORTANT update the list before use it.
        """

        #update the list from the webpage before use it to avoid type errors
        list_currencies= ['AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK',
        'EUR','GBP','HKD','HRK','HUF','IDR','ILS','INR','ISK','JPY','KRW',
        'MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK','SGD','THB',
        'TRY','USD','ZAR']

        self.assertEqual(isinstance(get_currencies(), list),True)
        self.assertEqual(get_currencies(),list_currencies)

