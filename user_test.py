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

  # Test to save user
  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user list
    '''
    self.new_user.save_user() # saving the new user
    self.assertEqual(len(User.user_list),1)


  # Setup and class creation up here
  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run
    '''
    User.user_list = []

  # Test to save more than one user
  def test_save_multiple_users(self):
    '''
    test_save_multiple_users to check if we can save multiple users object to our user_list
    '''
    self.new_user.save_user()
    test_user = User("John", "Doe", "0712344556") # New user
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)


if __name__ == '__main__':
  unittest.main()