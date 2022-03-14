import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will print an error message.

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    if lenght of the input arguments is equal to 3 (main + currency_from + currency_to) 
        if the 2 codes are different :
            call the get_rate() method with the 2 input arguments given and return the formatted result
        if the 2 codes are the same:
            return a message: you provide the same currency codes
    if lenght of the of the input arguments is less or more than 3:
            return an error message: you do not provide 2 currency codes
        
    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student
    if len(sys.argv) == 3:
        if (str(sys.argv[1]) != str(sys.argv[2])):
            return print(get_rate(sys.argv[1], sys.argv[2]))
        
        elif (str(sys.argv[1]) == str(sys.argv[2])):
            return print("[ERROR] You provided the same 2 currency codes")
    
    if len(sys.argv) < 3 or len(sys.argv)>3:
        return print("[ERROR] You haven't provided 2 currency codes")

def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    if from_currency and to_currency are in the available currency list:
        1. Using format_latest_url() format the url with the from_currency and to_currency arguments
           to then use call_api() ti call the API endpoint and get the response.
        2. If the call_api object has status_code=200 (no error)
            1. Using extract_api_result() transform the response to json to then extract the results
               and create a Currency class. 
            2. Using format_result() from Currency Class create the formatted final message 
               using its attributes.
        3. If the call_api object has status_code different of 200 (error)
            1. return the error (status_code)
    if from_currency is not in the availble currency list but to_currency is:
        Return the message "It is not a valid option"
    if to_currency is not in the availble currency list but from_currency is:
        Return the message "It is not a valid option"
    else:
        Return the message "They are not a valid option"

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student

    if (check_valid_currency(from_currency)==True) and (check_valid_currency(to_currency) ==True):
        
        called_api = call_api(format_latest_url(from_currency,to_currency))

        #looking the status_code from call_api 
        #it could not be done in call_api because it return a requests.models.Response
        if called_api.status_code == 200:
            return extract_api_result(called_api.json()).format_result()
        else:
            return f"There is an error with API call. ERROR: {called_api.status_code}"


    elif (check_valid_currency(from_currency)==True) and (check_valid_currency(to_currency) != True):
        return f"{to_currency} is not a valid option. Please type another one."

    elif (check_valid_currency(from_currency)!=True) and (check_valid_currency(to_currency) == True):
        return f"{from_currency} is not a valid option. Please type another one."

    else:
        return f"{from_currency} and {to_currency} are not valid options. Please type other ones."

if __name__ == "__main__":
    main()
