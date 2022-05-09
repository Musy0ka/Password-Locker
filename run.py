#!/usr/bin/env python3.8

from user import User

def create_user (fname,lname,phone,password):
  '''
  Function to create a new user
  '''

  new_user = User (fname, lname, phone, password)
  return new_user