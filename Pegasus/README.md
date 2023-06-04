Pegasus PostgreSQL Audit is a command-line tool for auditing a PostgreSQL database. It provides various audit functionalities to check roles, privileges, activities, security configurations, default passwords, database size, and long-running transactions.

## Requirements

- Python 3.x
- psycopg2 library
- pyfiglet library
- argparse library

## Installation

1. Clone the repository:
git clone url

2. pip install -r requirements.txt

3. Usage :
python audit.py -u <username> -pass <password> -ip <host> -db <database>


Example :

└─$ python Pegasus.py
 ____                                
|  _ \ ___  __ _  __ _ ___ _   _ ___ 
| |_) / _ \/ _` |/ _` / __| | | / __|
|  __/  __/ (_| | (_| \__ \ |_| \__ \
|_|   \___|\__, |\__,_|___/\__,_|___/
           |___/                     

Pegasus PostgreSQL Audit v.1.0


usage: Pegasus.py [-h] -u USER -pass PASSWORD -ip HOST -db DATABASE
Pegasus.py: error: the following arguments are required: -u, -pass, -ip, -db

