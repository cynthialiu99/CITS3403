import unittest, os
from app import flaskApp, db
from app.models import User
from config import TestConfig

class UserModelCase(unittest.TestCase):
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
    
    if __name__ == '__main__':
        unittest.main()