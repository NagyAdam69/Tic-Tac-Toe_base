def get_menu_option():
  '''
  Should print a menu with the following options:
  print("1. Human vs Human")
  print("2. Random AI vs Random AI")
  print("3. Human vs Random AI")
  print("4. Human vs Unbeatable AI")
  
  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  jatekmod = 0
  print('\t1. Human vs Human \n\t2. Random AI vs Random AI \n\t3. Human vs Random AI\n\t4. Human vs Unbeatable AI')
  
  while True:
      try:
          jatekmod = int(input("Choose a gamemode (1-4): "))
          if 1 <= jatekmod <= 4:
              return jatekmod
          else:
              print("Invalid input. Please choose a number between 1 and 4.")
      except ValueError:
          print("Invalid input. Please enter a number between 1 and 4.")


""""
  # run this file to test you have implemented correctly the function
  option = get_menu_option()
  print("If the user selected 1, it should print 1")
  print(option) """

get_menu_option()