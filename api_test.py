import unittest
from app.DB import book_info

expected_data = {
    547: {"title": "1984", "price": 9.99},
    288: {"title": "CATCH-22", "price": 9.99},
    484: {"title": "No title", "price": 9.99},
    899: {"title": "IT", "price": 9.99},
    773: {"title": "DO ANDROIDS DREAM OF ELECTRIC SHEEP", "price": 9.99}
}


class test_book_info(unittest.TestCase):
    # Test to check if all the data in the books table returns the correct data
    def test_ids(self):
        for data in expected_data.items():
            self.assertEqual(book_info(data[0]), data[1])

    # Test to check if an unknown book returns an empty JSON object
    def test_unknown_id(self):
        self.assertEqual(book_info(0), {})

if __name__ == '__main__':
    unittest.main()
