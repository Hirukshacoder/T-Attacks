import random
print("  ______    ___   __  __             __       ")  
print(" /_  __/   /   | / /_/ /_____ ______/ / _____  ")
print("  / /     / /| |/ __/ __/ __ `/ ___/ //_/ ___/ ")
print(" / /     / ___ / /_/ /_/ /_/ / /__/ ,< (__  ) ")
print("/_/     /_/  |_\__/\__/\__,_/\___/_/|_/____/ ") 

print("") 
print("")

name = input("Enter your name: ")
grettings = 'HI', 'Hello', 'Nice to meet you'
gret_with = random.choice(grettings)
print(gret_with, name, ", Welcome to T Attacks")
print("")
print("")

print("[1] Email Attacker")
print("[2] phone number locator")
print("")

select_option = input("Enter the the option you want: ")

if select_option == '1':
    print("")
    print("")
    print("Email Attacker was chosen")
    print("")
    print("")
    from email_attacker import *
    
else:
 if select_option == '2':
    print("")
    print("phone number locator was chosen")
    print("")
    from phonenumberlocator import *
    
  else:
     print("Nothing found")
     print("Good bye!")
