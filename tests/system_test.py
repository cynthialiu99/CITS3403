import unittest
import os
import time
from app import create_app, db
from app.models import User
from app.config import TestConfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

basedir = os.path.abspath(os.path.dirname(__file__))
local_host = "http://localhost:5000/"

class SystemTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")  
        chrome_options.add_argument("--disable-gpu")  
        chrome_options.add_argument("--headless")  
        cls.driver = webdriver.Chrome(options=chrome_options)
        if not cls.driver:
            raise unittest.SkipTest('Could not create driver')

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        users = User.query.all()
        if users:
            self.skipTest('Database is not empty')
        db.session.query(User).delete()
        staff = User(username='01234567', email='01234567@uwa.edu.au', points=0, status='staff')  # Adjusted for consistency
        staff.set_password('staffpassword')
        db.session.add(staff)
        db.session.commit()
        self.driver.maximize_window()
        self.driver.get(local_host)

    def tearDown(self):
        if self.driver:
            db.session.query(User).delete()
            db.session.commit()
            db.session.remove()
        self.app_context.pop()

    def test_signup(self):
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicitly_wait(5)
        # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'username')))

        username_field = self.driver.find_element(by='name', value='username')
        username_field.send_keys('23456789')
        email_field = self.driver.find_element(by='name', value='email')
        email_field.send_keys('23456789@student.uwa.edu.au')
        password_field = self.driver.find_element(by='name', value='password')
        password_field.send_keys('testpassword')
        confirm_field = self.driver.find_element(by='name', value='password2')
        confirm_field.send_keys('testpassword')
        time.sleep(1)
        submit = self.driver.find_element(by='class name', value='sign-up-button')
        submit.click()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_partial_link_text('Logout')
        self.assertTrue(logout.is_displayed())


    def test_logout(self):
        self.driver.get('http://localhost:5000/login')
        username_field = self.driver.find_element(by='name', value='username')
        username_field.send_keys('01234567')
        password_field = self.driver.find_element(by='name', value='password')
        password_field.send_keys(by='name', value='staffpassword')
        submit_button = self.driver.find_element(by='name', value='submit')
        submit_button.click()
        self.driver.find_element_by_partial_link_text('Logout').click()
        self.driver.implicitly_wait(5)
        login_link = self.driver.find_element_by_partial_link_text('Login')
        self.assertTrue(login_link.is_displayed())

    def test_invalid_signup(self):
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicitly_wait(5)
        username_field = self.driver.find_element(by='name', value='username')
        username_field.send_keys('existing_user')
        email_field = self.driver.find_element(by='name', value='email')
        email_field.send_keys('existing_user@example.com')
        password_field = self.driver.find_element(by='name', value='password')
        password_field.send_keys('testpassword')
        confirm_field = self.driver.find_element(by='name', value='password2')
        confirm_field.send_keys('testpassword')
        submit_button = self.driver.find_element(by='name', value='submit')
        submit_button.click()
        error_message = self.driver.find_element_by_class_name('error').text
        self.assertEqual(error_message, 'Username or email already exists.')

    def test_homepage_redirect(self):
        self.driver.get('http://localhost:5000/login')
        username_field = self.driver.find_element(by='name', value='username')
        username_field.send_keys('01234567')
        password_field = self.driver.find_element(by='name', value='password')
        password_field.send_keys('staffpassword')
        submit_button = self.driver.find_element(by='name', value='submit')
        submit_button.click()
        self.driver.implicitly_wait(5)
        self.assertIn('Home', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
