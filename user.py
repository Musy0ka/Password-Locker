class User:
  '''
  Class that generates new instances of user
  '''

  user_list = [] # Empty user list

  # Init method
  def __init__ (self, first, last, phone_number, password):
    self.first = first
    self.last = last
    self.phone_number = phone_number
    self.email = first + '.' + last + '@myspace.com'
    self.password = password



  def save_user(self):
    '''
    save_user method saves user info into the user_list
    '''

    User.user_list.append(self)



  def delete_user(self):
    '''
    Delete_user method deletes a saved user from the user_list
    '''

    User.user_list.remove(self)

  

  @classmethod
  def user_exists(cls, number):
    '''
    Method that checks if a user exists from the user_list

    Args:
          number: Phone number to search if it exists

    Returns:
            Boolean: True or False depending if the user exists
    '''

    for user in cls.user_list:
      if user.phone_number == number:
        return True

    return False



  @classmethod
  def display_users(cls):
    '''
    Method that returns that user list
    '''

    return cls.user_list



#The credentials class will contain the credentials ie username and password
#of the user from various platforms. It will also generate new passwords
#Objective is to store generic username and password for existing platforms and create
#new credentials for new accounts using password and auto generate passwords

class Credentials(User):
  '''
  Credentials class that stores user credentials from various platforms
  '''

  credentials_list = []

  '''
  Empty list to store credentials
  '''

  def __init__ (self, first, last, phone_number, platform, acc_username, acc_password):

    '''
    Constructor to generate new credentials for every platform

    Takes in the name of the username and password and platform
    '''

    super().__init__(first, last, phone_number)

    '''
    Used super to call parents init method
    '''
    self.platform = platform
    self.username = acc_username
    self.Password = acc_password