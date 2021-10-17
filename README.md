# Gemini-DCA

## About

Purchase Crypto with the lowest(?) available fees by using the Gemini API.
Achieved by placing Maker or Cancel orders just below the current price securing 0.1% fees or lower.

Gemini's support for up to 10 free withdrawals per month make this method ideal for DCA or quick purchasing.

## References & Links

More information about Gemini Fees:
https://www.gemini.com/fees/api-fee-schedule


Original code modified from:
https://www.youtube.com/watch?v=h6r1h3am6kA

Video includes instructions for running code on AWS rather than personal server.


https://www.gemini.com/share/axdlekncd

Get $10 in BTC when you trade $100 after sign up.

## Setup
Create Primary API key for Gemini with fund management and trading permission.

Copy the key and private key into secrets.py file.

Automate DCA purchase timing using Crontab.
