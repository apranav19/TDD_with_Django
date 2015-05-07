from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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

        #self.assertEqual(input_box.get_attribute('placeholder'), "Enter a to-do item")

        # Buy an item
        #input_box.send_keys('Buy an item')

        # When a user hits ENTER, the page must update
        # to display a table of to-do items
        #input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy an item', [row.text for row in rows])

        # Test 2nd item
        self.assertIn('2: Sell an item', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
