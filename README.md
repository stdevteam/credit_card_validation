=================
Credit Card Validation
=================

-----------------
Development setup
-----------------
Install required system packages:

.. code-block:: bash
$ sudo apt-get install python3-pip
$ sudo apt-get install python3.6-dev
$ pip install -r requirements.txt

-----------------
Project Description 
-----------------

A validate credit cards

► It must start with a 4, 5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of digits (0-9). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ', '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.


-----------------
CLI commands
-----------------

To check one card number:

$ python main.py check_card_number CARD_NUM

To check several card numbers, 
you need to set the number of cards and then enter the numbers

$ python main.py input_cards_count CARDS_COUNT


-----------------
Unit Tests
-----------------

To run unit tests:

$ python test.py

-----------------
[Project Documentation](./Short-test-python-20190803.docx)
-----------------