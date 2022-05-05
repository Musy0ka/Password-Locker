import unittest # Importing the unittest module
from user import User

class TestUser(unittest.TestCase):

  def setUp(self):
    '''
    SetUp method to run before test cases
    '''

    self.new_user = User ('Allan', 'Musyoka', '0729789761') # Create contact object


  def test_init(self):
    self.assertEqual(self.new_user.first,"Allan")
    self.assertEqual(self.new_user.last,"Musyoka")
    self.assertEqual(self.new_user.phone_number,"0729789761")


if __name__ == '__main__':
  unittest.main()