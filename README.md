# eth-identity-registry
Ethereum Identity Management

# Installation
* pip install -r requirement.txt
* populus chain init local_test (or run on mainnet or morden)
* populus compile
* populus deploy  --chain local_test
* Run ./manage.py runserver

# Command line

* python run.py register 0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03 test@test.com
* python run.py verify 0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03 test@test.com
* python run.py remove test@test.com
* python run.py owner test@test.com
