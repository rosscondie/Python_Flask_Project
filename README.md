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

You should see this in your terminal: 
```bash
# terminal 
 * Serving Flask app 'app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:4999
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 453-664-860
 ```
 
 You can click on the link to open app in your browser:
 ```bash
 # terminal
 * Running on http://127.0.0.1:4999
 ```




