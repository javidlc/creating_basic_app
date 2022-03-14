import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'

def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    1.Try to make a request to a web page using a specific url and saved the response 
        (not mandatory to save it, only to show the type)
        if there is no connection raise the error and exit the program
    2. Print the type of the response to check if it is a requests.models.Response (uncomment to use it)

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    # => To be filled by student
    try:
        resp = requests.get(url)
        #print(f"call_api request type is {type(resp)}")
        return resp
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    Create a string joining:
        - The frankfurter.app url until its Top-level Domain
        (_HOST_ variable given) 
        - The currency endpoint 
        (_CURRENCIES_ variable given is the Subdirectory part of the url with all the available currencies)

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    # => To be filled by student
    return _HOST_ + _CURRENCIES_


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    1. Using format_currencies_url() format the url to be passed into call_api() to call 
    the endpoint and return the response.
    2. Get the response as a json and get the currency symbols (keys of the json). 
    (The values of these keys are the full names: See 'https://api.frankfurter.app/currencies')
    3. Create a list of this dict_keys.

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # => To be filled by student
    return list(call_api(format_currencies_url()).json().keys())


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    Create a string joining: 
        - The frankfurter.app url until its Top-level Domain 
        (_HOST_ variable given) 
        - The latest endpoint 
        (_LATEST_ variable given is the first part of the url subdirectory) 
        - The specific currencies given as input arguments 
        (from_currency and to_currency are the second part of the url subdirectory)

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # => To be filled by student   

    return _HOST_ + _LATEST_+ '?from=' + from_currency + '&to=' + to_currency


