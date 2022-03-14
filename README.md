<h1 align="center">Currency Converter in Python</h1>

## Author

**Javiera de la Carrera**

- Student ID: 13743354
- Email: javiera.delacarreragarcia@student.uts.edu.au

## Description
The app is built to perform currency conversion using data from an open-source API [Frankfurter](https://www.frankfurter.app/). In more details, the objective is to display the current conversion rate between 2 currency codes given by the user and also calculate the inverse conversion rate between them.

Three files composed the python program described below (main.py, api.py and currency.py). 
Besides, three files with unittests were created to check if program functions operates in the right way.

## Available Commands

In the project directory, you can run:

### `python main.py AUD EUR`

(you can type whatever currencies you want to get the conversion rate)

If you are using Pipenv, then you can run after install pipenv:

### `pipenv install`
### `pipenv run python main.py AUD EUR`

Also, you can run the following to test the functions:

### `python -m unittest`

## Built With

- python 3.7.9

## Package Dependencies

- requests 2.26.0

## Structure

    ├── api.py             
    ├── currency.py        
    ├── main.py            
    ├── Pipfile            
    ├── Pipfile.lock       
    ├── README.md          
    ├── test_api.py        
    ├── test_main.py       <- File with Unit tests to check if get_rate funtion is working as expected.
    └── test_currency.py   