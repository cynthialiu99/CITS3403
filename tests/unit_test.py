import unittest, os
from unittest import TestCase
from app import flaskApp, db, create_app, test_data
from app.models import User
from app.__init__ import TestConfig

class UserModelCase(TestCase):
    def setUp(self):
        self.app = flaskApp.test_client()
        db.create_all()
        user1 = User(id = 0, username='25123456', email='25123456@student.uwa.edu.au', staff=False)
        user2 = User(id = 1, username='08679768', email='08679768@uwa.edu.au', staff=True)
        user1.set_password('testpassword')
        user2.set_password('password2')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hash(self):
        user = User.query.get(0)
        user.set_password('correct')
        self.assertFalse(user.check_password('wrong'))
        self.assertTrue(user.check_password('correct'))

    def test_is_committed(self):
        user = User.query.get(0)
        self.assertFalse(user.is_committed())
        user2 = User.query.get(1)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        self.assertTrue(user.is_committed())

    def test_set_password(self):
        user = User(username='02345678', email='02345678@uwa.edu.au', staff=True)
        user.set_password('testpassword')
        self.assertTrue(user.check_password('testpassword'))

    def test_email_uniqueness(self):
        # Attempt to create two users with the same email
        user1 = User(username='user1', email='23066191@student.uwa.edu.au', staff=False)
        user2 = User(username='user2', email='23066191@student.uwa.edu.au', staff=False)
        db.session.add(user1)
        db.session.add(user2)
        with self.assertRaises(Exception):
            db.session.commit()
    
    def test_username_length(self):
        # Attempt to create a user with a username longer than the maximum allowed length
        long_username = 'a' * 65  # Assuming maximum length is 64
        user = User(username=long_username, email='test@example.com', staff=False)
        with self.assertRaises(ValueError):
            db.session.add(user)
            db.session.commit()
    
    if __name__ == '__main__':
        unittest.main()
