import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """ Is name Title case"""

        formatted_name = get_formatted_name('amaka', 'chilaka')
        self.assertEqual(formatted_name, 'Amaka Chilaka')

    def test_first_last_middle_name(self):
        """Do first, last and middle name work?"""

        formatted_name = get_formatted_name(
            'amaka','chilaka', 'miriam')
        self.assertEqual(formatted_name, 'Amaka Miriam Chilaka')



if __name__ == '__main__':
    unittest.main()

