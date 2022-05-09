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


def display_users():
  '''
  Function that returns all the saved users
  '''

  return User.display_users()




def main():
  print("Wagwan User Welcome to your user list. Please enter your name?")
  
  user_name = input()

  print(f"Hello {user_name}. What you care to do this moment?")
  print('\n')

  while True:
    print("Use These short codes: cc - create a new user, dc - display users, fc - find a user, ex - exit")

    short_code = input().lower()

    if short_code == 'cc':
      print("New User")
      print("-" * 10)

      print("First name .....")
      f_name = input()

      print("Last name .....")
      l_name = input()

      print ("Phone number .....")
      p_number = input()

      print ("Pasword .....")
      password = input()

      # Create and save new user
      save_users(create_user(f_name, l_name, p_number, password))
      print('\n')
      print(f"New User {f_name} {l_name} has been created")
      print('\n')

    # Display saved users
    elif short_code == 'dc':
      if display_users():
        print("Below is a list of your users")
        print('\n')

        for user in display_users():
          print(f"{user.first_name} {user.last_name} ->  {user.phone_number}")

        print('\n')


      else:
        print('\n')
        print("You don't seem to have any user saved yet")

        print('\n')


    # #Search for user using phone number
    # elif short_code == 'fc':
    #   print("Enter the new number that you would like to search for")

    #   search_number = input()
    #   if check_existing_users(search_number):
    #     search_user = find_user (search_number)

    #     print(f"{search_user.first_name} {search_user.last_name}")

    #     print('-' * 20)

    #     print(f"Phone Number .........{search_user.phone_number}")
        
      
    #   else:
    #     print("The user entered does not exist")


    elif short_code == "ex":
      print("Bye Nigger ..... Catch you on the flip side")
      break

    else:
      print("I really don't seem to gerrit. Please use the correct short codes")


if __name__ == '__main__':
  main()