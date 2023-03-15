# Python Flask Project 

Travel Bucket List CRUD app made in Python with Flask, using a PostgreSQL database.

#### Technologies used:
- Python 3
- Flask
- psycopg2
- PostgreSQL
- HTML
- CSS

## Setup Instructions

To install:

```bash
# terminal
pip3 install psycopg2
pip3 install Flask
```

You will need to create a PostgreSQL database called `travel_manager`:

```bash
# terminal
createdb travel_manager
```

Then setup the tables:

```bash
# terminal
psql -d travel_manager -f db/travel_manager.sql
```

Seed the data:

```bash 
# terminal
python3 seeds.py
```

To run the app:
```bash
# terminal
flask run
```




