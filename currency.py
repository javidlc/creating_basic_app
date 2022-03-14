from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    1. Transform currency input to uppercase to avoid failures
    2. Check if the transformed currency is in the list created in get_currencies() method 
    named CURRENCIES in this script.

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    # => To be filled by student
    return currency.upper() in CURRENCIES


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when conversion rate was recorded.
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # => To be filled by student
        self.inverse_rate = round((1/ self.rate),5)

    def format_result(self):
        """
        Method returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        # => To be filled by student
        return f"Today's ({self.date}) conversion rate from {self.from_currency} to {self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}."

def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Currency code to be converted from

    Pseudo-code
    ----------
    Instantiate a Currency class and fill it with the values from the argument(result):
        1. Get amount, from_currency, date and to_currency
        1. From rates dictionary in the result, get the keys as the to_currency 
           and create a list to get the first value.
        2. From rates dictionary in the result, get the value as the rate and create a list 
           to get the first value and transform it to float (important to the inverse_rate code).
    Add the inverse_rate attribute to the currency class created throught the reverse_rate() method.

    Returns
    -------
    Currency
        Instantiated Currency
    """
    # => To be filled by student
    #extracting relevant fields
    currency = Currency(amount = result.get("amount"),
                        from_currency = result.get("base"),
                        date = result.get("date"),
                        to_currency =list(result.get("rates").keys())[0], 
                        rate = float(list(result.get("rates").values())[0]))

    currency.reverse_rate()

    return currency
