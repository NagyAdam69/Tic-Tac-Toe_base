def get_menu_option():
  '''
  Should print a menu with the following options:
  print("1. Human vs Human\n")
  print("2. Random AI vs Random AI\n")
  print("3. Human vs Random AI\n")
  print("4. Human vs Unbeatable AI\n")

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 