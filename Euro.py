import random
import os
from tabulate import tabulate

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

score=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7]
    
#instert matches played to table
def mp():
    i[0][1] = i[0][1]+1
    i[1][1] = i[1][1]+1

#insert win, lose, draw and points to table
def wld_pts():
    if score1==score2:
        i[0][3] = i[0][3]+1
        i[1][3] = i[1][3]+1
        i[0][8] = i[0][8]+1
        i[1][8] = i[1][8]+1
    elif score1>score2:
        i[0][2] = i[0][2]+1
        i[1][4] = i[1][4]+1
        i[0][8] = i[0][8]+3
        i[1][8] = i[1][8]+0
    elif score1<score2:
        i[0][4] = i[0][4] + 1
        i[1][2] = i[1][2] + 1
        i[0][8] = i[0][8] + 0
        i[1][8] = i[1][8] + 3

#insert gf ga and gd into table
def gf_ga_gd():
    i[0][5] = i[0][5] + score1
    i[1][5] = i[1][5] + score2

    i[0][6] = i[0][6] + score2
    i[1][6] = i[1][6] + score1

    i[0][7] = i[0][5] - i[0][6]
    i[1][7] = i[1][5] - i[1][6]




game=True
while game:
    pick24()
    group_a=[]
    group_b=[]
    group_c=[]
    group_d=[]
    group_e=[]
    group_f=[]
    os.system('cls')
    os.system('clear')

    year=year+4
    make_groups()
    
    print ("\nWelcome to UEFA Euro ",(year), "in", random.choice(group_b))

    

    print ("Teams that will play in Euro: ")
    print_groups()
   
    print("--------------------")

    """full_or_results=input("Type \"w\" to see whole Euro or \"r\" if you want to see just the results: ")
    while not (full_or_results == "w" or full_or_results == "r"):
        full_or_results = input("Type \"w\" for whole Euro or \"r\" for winner: ")
    full_or_results=full_or_results"""

    input("\nHit enter to see group stage")
    os.system('cls')
    os.system('clear')

   #group A

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_a[0]=[group_a[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_a[1]=[group_a[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_a[2]=[group_a[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_a[3]=[group_a[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpa=[[group_a[0], group_a[1]], [group_a[2], group_a[3]], [group_a[0], group_a[2]],[group_a[1], group_a[3]], [group_a[0], group_a[3]], [group_a[1], group_a[2]]]
    print("----------\nGroup A matches\n----------")
    
    for i in grpa:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_a.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_a, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_a[0][0]),"and", group_a[1][0])

    input("\nHit enter to see Group B")
    os.system('cls')
    os.system('clear')

    #group B

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_b[0]=[group_b[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_b[1]=[group_b[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_b[2]=[group_b[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_b[3]=[group_b[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpb=[[group_b[0], group_b[1]], [group_b[2], group_b[3]], [group_b[0], group_b[2]],[group_b[1], group_b[3]], [group_b[0], group_b[3]], [group_b[1], group_b[2]]]
    print("----------\nGroup B matches\n----------")
    
    for i in grpb:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_b.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_b, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_b[0][0]),"and", group_b[1][0])

    input("\nHit enter to see Group C")
    os.system('cls')
    os.system('clear')
    
    #group C

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_c[0]=[group_c[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_c[1]=[group_c[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_c[2]=[group_c[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_c[3]=[group_c[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpc=[[group_c[0], group_c[1]], [group_c[2], group_c[3]], [group_c[0], group_c[2]],[group_c[1], group_c[3]], [group_c[0], group_c[3]], [group_c[1], group_c[2]]]
    print("----------\nGroup C matches\n----------")
    
    for i in grpc:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_c.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_c, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_c[0][0]),"and", group_c[1][0])

    input("\nHit enter to see Group D")
    os.system('cls')
    os.system('clear')

    #group D

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_d[0]=[group_d[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_d[1]=[group_d[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_d[2]=[group_d[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_d[3]=[group_d[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpd=[[group_d[0], group_d[1]], [group_d[2], group_d[3]], [group_d[0], group_d[2]],[group_d[1], group_d[3]], [group_d[0], group_d[3]], [group_d[1], group_d[2]]]
    print("----------\nGroup D matches\n----------")
    
    for i in grpd:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_d.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_d, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_d[0][0]),"and", group_d[1][0])

    input("\nHit enter to see Group E")
    os.system('cls')
    os.system('clear')

    #group E

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_e[0]=[group_e[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_e[1]=[group_e[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_e[2]=[group_e[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_e[3]=[group_e[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpe=[[group_e[0], group_e[1]], [group_e[2], group_e[3]], [group_e[0], group_e[2]],[group_e[1], group_e[3]], [group_e[0], group_e[3]], [group_e[1], group_e[2]]]
    print("----------\nGroup E matches\n----------")
    
    for i in grpe:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_e.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_e, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_e[0][0]),"and", group_e[1][0])

    input("\nHit enter to see Group F")
    os.system('cls')
    os.system('clear')

    #group F

    headers=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    group_f[0]=[group_f[0], 0, 0, 0, 0, 0, 0, 0, 0]
    group_f[1]=[group_f[1], 0, 0, 0, 0, 0, 0, 0, 0]
    group_f[2]=[group_f[2], 0, 0, 0, 0, 0, 0, 0, 0]
    group_f[3]=[group_f[3], 0, 0, 0, 0, 0, 0, 0, 0]

    grpf=[[group_f[0], group_f[1]], [group_f[2], group_f[3]], [group_f[0], group_f[2]],[group_f[1], group_f[3]], [group_f[0], group_f[3]], [group_f[1], group_f[2]]]
    print("----------\nGroup F matches\n----------")
    
    for i in grpf:
          score1=(random.choice(score))
          score2=(random.choice(score))
          mp()
          wld_pts()
          gf_ga_gd()
          print(i[0][0], i[1][0], sep="   vs   ")
          print(score1,":",score2)

    group_f.sort(key=lambda team: (team[8], team[7]), reverse=True)
    print("\n")
    print(tabulate(group_f, headers=["Team", "MP", "W ", "D ", "L ", "GF", "GA", "GD", "Pts"],))
    
    print ("\nTeams getting promoted are:", (group_f[0][0]),"and", group_f[1][0])








    print("--------------------\n")
    again=input("Would you like to see next Euro? y/n: ")
    if again=="y" or again=="Y":
      game=True
      os.system('cls')
      os.system('clear')
    else:
      print("\nHave a nice day then ;-)")
      game=False


