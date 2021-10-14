import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# DB info
URI = os.getenv("DATABASE_URL")

def book_info(id):
    """
        Function to query the Postgres table with given book id to return that
        book's price and title
        Inputs: id - The book id the user is trying to retrieve info from
        Output: JSON of the price and title of a book
    """
    # Create the DB connection
    # conn = psycopg2.connect(dbname=DBNAME, user=USER,
    #                         password=PASSWORD, host=HOST, port=PORT)

    conn = psycopg2.connect(URI)

    # Create the cursor
    cur = conn.cursor()

    # Query to retrieve the book's price and title given it's id
    query = f"""SELECT
    CASE
		WHEN price IS NULL THEN price
		WHEN price IS NOT NULL THEN ABS(price::FLOAT)
	END,
	CASE
		WHEN title IS NULL THEN 'No title'
		WHEN title IS NOT NULL THEN title
	END
    FROM books
    WHERE id = {id}
    """

    # Execute the query
    cur.execute(query)

    # Fetch the returned data from the query
    data = cur.fetchone()

    # If the book exists then create a JSON object with the data
    if data:
        book = {
            "price": data[0],
            "title": data[1]
        }

    # If the book does not exist then return an empty JSON object
    else:
        return {}

    # Close the connection
    conn.close()

    # Return the JSON containing the book's price and title
    return book
