# Bob's book club API

## Local setup

 - Clone the repo and cd into the directory
 - Either run `pip install -r requirements.txt` directly or create a pipenv with Python version 3.6 and install requirements.txt
 - `export/set FLASK_APP=microblog.py` to set the FLASK_APP environment variable
 - `flask run` to run the flask API

## Tech Stack

 - Languages: Python 3.6, SQL 
 - API Framework: Flask
 - Deployment: Heroku
 - Database: Postgres
 
## Endpoint
### /book/<id (int)>
 - A get request that allows the user to enter a book's id to return that specific book's price and title in a JSON object.
	 - Entering a non-integer will return a 404 error
 - If the user enters a book id that does not exist in the database then it will return a empty JSON object .
 - price is a float and title is a string.
 - Example Response:
 
```
{"price": 9.99,
"title": "1984"}
```
