#!/usr/bin/env python3.8

from user import User

def create_user (fname,lname,phone,password):
  '''
  Function to create a new user
  '''

  new_user = User (fname, lname, phone, password)
  return new_user

def save_users(user):
  '''
  Function to save user
  '''

  user.save_user()

def delete_user(user):
  '''
  Function to delete a user
  '''

  user.delete_user()


def check_existing_users(number):
  '''
  Function that check if a user exists with that number and returns a Boolean
  '''

  return User.user_exists(number)