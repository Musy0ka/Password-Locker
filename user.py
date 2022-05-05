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

