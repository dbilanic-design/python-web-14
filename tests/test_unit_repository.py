import unittest
from app.crud import create_contact

class TestRepository(unittest.TestCase):

    def test_create_contact(self):
        db = FakeDB()

        contact = FakeContact(
            first_name="Test",
            last_name="User"
        )

        result = create_contact(db, contact, 1)

        self.assertEqual(result.first_name, "Test")
