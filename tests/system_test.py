import unittest, os, time
from app import flaskApp, db, create_app
from app.models import User
from app.__init__ import TestConfig
from selenium import webdriver

basedir = os.path.abspath(os.path.dirname(__file__))
local_host = "http://localhost:5000/"

class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(basedir,))
        
        if not self.driver:
            self.skipTest('Could not create driver')
        else:
            db.init_app(flaskApp)
            db.create_all()
            users = User.query.all()
            if users:
                self.skipTest('Database is not empty')
            db.session.query(User).delete()
            staff = User(username='01234567', email='01234567@uwa.edu.au', staff=True)
            staff.set_password('staffpassword')
            db.session.add(staff)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get(local_host)

    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.query(User).delete()
            db.session.commit()
            db.session.remove()

    def test_signup(self):
        user = User.query.get(0)
        self.assertEqual(user.username,'staff',msg='user exist.')
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicity.wait(5)
        username_field = self.driver.find_element_by_id('username')
        user.username.send_keys('23456789')
        email_field = self.driver.find_element_by_id('student')
        user.email.send_keys('@student.uwa.edu.au')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('testpassword')
        confirm_field = self.driver.find_element_by_id('password2')
        confirm_field.send_keys('testpassword')
        time.sleep(1)
        self.driver.implicity_wait(5)
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        self.driver.implicity_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_partial_link_text('logout')
        self.assertEqual(logout.get_attribute('innerHTML')),'logout user'

    def test_logout(self):
        self.driver.get('http://localhost:5000/login')
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys('01234567')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('staffpassword')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        self.driver.find_element_by_partial_link_text('Logout').click()
        self.driver.implicitly_wait(5)
        login_link = self.driver.find_element_by_partial_link_text('Login')
        self.assertTrue(login_link.is_displayed())

    def test_invalid_signup(self):
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicitly_wait(5)
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys('existing_user')  # Assuming 'existing_user' already exists in the database
        email_field = self.driver.find_element_by_id('student')
        email_field.send_keys('existing_user@example.com')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('testpassword')
        confirm_field = self.driver.find_element_by_id('password2')
        confirm_field.send_keys('testpassword')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        error_message = self.driver.find_element_by_class_name('error').text
        self.assertEqual(error_message, 'Username or email already exists.')

    def test_homepage_redirect(self):
        self.driver.get('http://localhost:5000/login')
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys('01234567')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('staffpassword')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        self.driver.implicitly_wait(5)
        self.assertTrue('Home' in self.driver.title)

    
    if __name__ == '__main__':
        unittest.main(verbosity=2)
