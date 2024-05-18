import unittest
import os
import time
from selenium import webdriver
from app import create_app, db
from app.models import User
from app.config import TestConfig  # Import TestConfig

basedir = os.path.abspath(os.path.dirname(__file__))
local_host = "http://localhost:5000/"

class SystemTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_class=TestConfig)  # Use the 'TestConfig' configuration
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless browser if needed
        self.driver = webdriver.Chrome(options=options)

        staff = User(id=0,username='01234567', password_hash = '4758', email='01234567@uwa.edu.au',points=5,status='yes')
        staff.set_password('staffpassword')
        db.session.add(staff)
        db.session.commit()
        self.driver.maximize_window()
        self.driver.get(local_host)

    def tearDOwn(self):
        if self.driver:
            self.driver.quit()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_signup(self):
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicitly_wait(5)
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys('23456789')
        email_field = self.driver.find_element_by_id('student')
        email_field.send_keys('23456789@student.uwa.edu.au')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('testpassword')
        confirm_field = self.driver.find_element_by_id('password2')
        confirm_field.send_keys('testpassword')
        time.sleep(1)
<<<<<<< Updated upstream
        self.driver.implicity_wait(5)
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        self.driver.implicity_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_partial_link_text('logout')
        self.assertEqual(logout.get_attribute('innerHTML')),'logout user',   
    
    if __name__ == '__main__':
        unittest.main(verbosity=2)
=======
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        self.driver.implicitly_wait(5)
        logout = self.driver.find_element_by_partial_link_text('Logout')
        self.assertEqual(logout.get_attribute('innerHTML'), 'Logout')

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
        username_field.send_keys('01234567')  # Assuming '01234567' already exists in the database
        email_field = self.driver.find_element_by_id('student')
        email_field.send_keys('01234567@student.uwa.edu.au')
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
        username_field = self.driver.find_element_by_id
>>>>>>> Stashed changes
