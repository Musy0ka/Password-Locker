class User:
  '''
  Class that generates new instances of user
  '''

  user_list = [] # Empty user list

  # Init method
  def __init__ (self, first, last, phone_number):
    self.first = first
    self.last = last
    self.phone_number = phone_number
    self.email = first + '.' + last + '@myspace.com'


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