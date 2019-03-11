=================
Credit Card Validation
=================

-----------------
Development setup
-----------------
Install required system packages:

.. code-block:: bash
```bash
sudo apt-get install python3-pip
sudo apt-get install python3.6-dev
pip install -r requirements.txt
 ```

-----------------
Project Description 
-----------------

Validate credit cards

<ol>
<li>It must start with a 4, 5 or 6.</li>
<li>It must contain exactly 16 digits.</li>
<li>It must only consist of digits (0-9).</li>
<li>It may have digits in groups of 4, separated by one hyphen "-". </li>
<li>It must NOT use any other separator like ' ', '_', etc. </li>
<li> It must NOT have 4 or more consecutive repeated digits.</li>
</ol


-----------------
CLI commands
-----------------

To check one card number:
```bash
python main.py check_card_number CARD_NUM
```
To check several card numbers, 
you need to set the number of cards and then enter the numbers

```bash
python main.py input_cards_count CARDS_COUNT
```


-----------------
Unit Tests
-----------------

To run unit tests:
```bash
python test.py
```

-----------------
[Project Documentation](docs/Short-test-python-20190803.docx)
-----------------