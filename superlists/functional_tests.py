from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Head over to the site
        self.browser.get('http://localhost:8000')

        # Check if title is customized
        self.assertIn('To-Do lists', self.browser.title)

        # Check if header is present
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User enters a to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Sell an item')
        input_box.send_keys(Keys.ENTER)

        # Use refactored method to check element in row
        self.check_for_row_in_list_table('1: Sell an item')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
