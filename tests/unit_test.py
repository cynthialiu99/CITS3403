import unittest
from app import create_app, db
from app.models import User
from app.config import TestConfig  # Import TestConfig

class UserModelCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_class=TestConfig)  # Use the 'TestConfig' configuration
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        user1 = User(id=1, username='25123456', email='25123456@student.uwa.edu.au')
        user2 = User(id=2, username='08679768', email='08679768@uwa.edu.au')
        user1.set_password('testpassword')
        user2.set_password('password2')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hash(self):
        user = User.query.get(1)
        user.set_password('correct')
        self.assertFalse(user.check_password('wrong'))
        self.assertTrue(user.check_password('correct'))

    def test_is_committed(self):
        user = User.query.get(1)
        self.assertFalse(user.is_committed())
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.is_committed())

    def test_set_password(self):
        user = User(username='02345678', email='02345678@uwa.edu.au')
        user.set_password('testpassword')
        self.assertTrue(user.check_password('testpassword'))

    def test_email_uniqueness(self):
        user1 = User(username='user1', email='23066191@student.uwa.edu.au')
        user2 = User(username='user2', email='23066191@student.uwa.edu.au')
        db.session.add(user1)
        db.session.add(user2)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_username_length(self):
        long_username = 'a' * 65
        user = User(username=long_username, email='test@example.com')
        with self.assertRaises(ValueError):
            db.session.add(user)
            db.session.commit()

if __name__ == '__main__':
    unittest.main()
