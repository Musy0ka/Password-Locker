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