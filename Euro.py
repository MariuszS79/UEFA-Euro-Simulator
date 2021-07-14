import random

uefa_member_countries=["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "England", "Estonia", "Faroe Islands", "Finland", "France", "Georgia", "Germany", "Gibraltar", "Greece", "Hungary", "Iceland", "Israel", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "North Macedonia", "Northern Ireland", "Norway", "Poland", "Portugal", "Republic of Ireland", "Romania", "Russia", "San Marino", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales"]

teams=random.sample(set(["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "England", "Estonia", "Faroe Islands", "Finland", "France", "Georgia", "Germany", "Gibraltar", "Greece", "Hungary", "Iceland", "Israel", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "North Macedonia", "Northern Ireland", "Norway", "Poland", "Portugal", "Republic of Ireland", "Romania", "Russia", "San Marino", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales"]), 24)

teams.sort()
print (*teams, sep=",")
random.shuffle(teams)

group_a=[]
group_b=[]
group_c=[]
group_d=[]
group_e=[]
group_f=[]

def make_groups():
  for i in range (4):
    group_a.append(teams.pop(-1))
    group_b.append(teams.pop(-1))
    group_c.append(teams.pop(-1))
    group_d.append(teams.pop(-1))
    group_e.append(teams.pop(-1))
    group_f.append(teams.pop(-1))
    
    

make_groups()
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
