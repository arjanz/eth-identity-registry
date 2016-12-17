# eth-identity-registry
Ethereum Identity Management

# Installation
* pip install -r requirement.txt
* cd eth_identity (where populus.ini resides)
* populus chain init local (or run on mainnet or morden)
* populus compile
* populus deploy  --chain local
* Run ./manage.py runserver --nothreading (or with gunicorn)

# Command line

* ./manage.py register_email test@test.com 0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03
* ./manage.py verify_email test@test.com 0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03
* ./manage.py remove_email test@test.com
