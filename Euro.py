import random
import os

uefa_member_countries=["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "England", "Estonia", "Faroe Islands", "Finland", "France", "Georgia", "Germany", "Gibraltar", "Greece", "Hungary", "Iceland", "Israel", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "North Macedonia", "Northern Ireland", "Norway", "Poland", "Portugal", "Republic of Ireland", "Romania", "Russia", "San Marino", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales"]

def pick24():
  global teams
  teams=random.sample(set(uefa_member_countries), 24)
  teams.sort()
  random.shuffle(teams)


year=2020


def make_groups():
  for i in range (4):
    group_a.append(teams.pop(0))
    group_b.append(teams.pop(0))
    group_c.append(teams.pop(0))
    group_d.append(teams.pop(0))
    group_e.append(teams.pop(0))
    group_f.append(teams.pop(0))

def print_groups():
  print("\nGroup A:")
  print (*group_a, sep="\n")
  print("-----\nGroup B:")
  print (*group_b, sep="\n")
  print("-----\nGroup C:")
  print (*group_c, sep="\n")
  print("-----\nGroup D:")
  print (*group_d, sep="\n")
  print("-----\nGroup E:")
  print (*group_e, sep="\n")
  print("-----\nGroup F:")
  print (*group_f, sep="\n")


    




game=True
while game:
    pick24()
    group_a=[]
    group_b=[]
    group_c=[]
    group_d=[]
    group_e=[]
    group_f=[]


    year=year+4
    make_groups()
    
    print ("\nWelcome to UEFA Euro ",(year), "in", random.choice(group_b))

    

    print ("Teams that will take part: ")
    print_groups()
   
    print("--------------------")

    full_or_results=input("Type \"f\" to see whole Euro or \"r\" if you want to see just the results: ")
    while not (full_or_results == "f" or full_or_results == "r"):
        full_or_results = input("Type \"f\" for whole Euro or \"r\" for winner: ")
    full_or_results=full_or_results


    print("--------------------\n")
    again=input("Would you like to see next Euro? y/n: ")
    if again=="y" or again=="Y":
      game=True
      os.system('cls')
      os.system('clear')
    else:
      print("\nHave a nice day then ;-)")
      game=False

