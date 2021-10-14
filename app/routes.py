from app import app
from .DB import book_info


# Default route for API
@app.route('/')
@app.route('/index')
def index():
    return "Bob's book club API is running!"


# Endpoint to return a book's price and title given the book's id
@app.route('/book/<int:id>', methods=['GET'])
def book(id):
    # Retrieve the book's price and title given it's id
    data = book_info(id)

    # Return the price and title of a book in a JSON format
    return data
