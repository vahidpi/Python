# Requirements
1. Core Functionality
The app should allow users to:

- Select or input a source currency (e.g., USD, EUR).
- Select or input a target currency (e.g., GBP, INR).
- Input the amount they want to convert.
- Fetch the exchange rate from an external API.
- Calculate and display the converted amount.

2. External API Integration
Use a currency exchange rate API to fetch real-time rates. Here are some free options:

- ExchangeRate-API https://www.exchangerate-api.com/
- Open Exchange Rates https://openexchangerates.org/
- CurrencyLayer https://currencylayer.com/



3. Build
- Need API Key
    - By registering in one of the listed services.
- Python env
    - source ~/path/to/venv/bin/activate
    - python3 -m pip install xyz
- Install necessary libraries:

    ``` pip install requests tkinter ```
    brew install python-tk