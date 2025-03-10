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
  def jatekmod_valasztas():
    while jatekmod_valasztas not in [1,2,3,4]:
      print("\nPlease choose from the listed options: ")
      print('\t1. Human vs Human \n \t2. Random AI vs Random AI \n \t3. Human vs Random AI\n \t4. Human vs Unbeatable AI')
      jatekmod = input("Choose a gamemode (1-4): ")
      return jatekmod



""""
  # run this file to test you have implemented correctly the function
  option = get_menu_option()
  print("If the user selected 1, it should print 1")
  print(option) """

get_menu_option()

