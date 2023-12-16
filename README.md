# Gemini-DCA

## About

Purchase Crypto with the lowest(?) available fees by using the Gemini API.

## References & Links

More information about Gemini Fees:
https://www.gemini.com/fees/api-fee-schedule


Original code modified from:
https://www.youtube.com/watch?v=h6r1h3am6kA

Video includes instructions for running code on AWS rather than personal server.


https://www.gemini.com/share/axdlekncd

Get $10 in BTC when you trade $100 after sign up.

## Setup
USE AT YOUR OWN RISK.

Create Primary API key for Gemini with fund management and trading permission.

Copy the key and private key into mysecrets.py file.

Automate crypto DCA purchase timing using Crontab.

## Logs
Run parse_logs.py to create .json and .csv files from .log files that include the successful transaction history.

These can be used to calculate cost basis in Google Sheets, Excel, or elsewhere.
