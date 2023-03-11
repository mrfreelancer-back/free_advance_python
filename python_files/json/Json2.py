from json import load as ld
from json import dumps as dmps

with open('D:\\free_advance_python\\python_files\\json\\people_inf.json') as json_file:
    data = ld(json_file)
    
print(data)

data2 = dmps(data)
print(data2)

for tow_person in data['people']:
    print(tow_person)
    
for first_inf in data['people'][0]:
    print(f"{first_inf} {data['people'][0][first_inf]}")

for second_inf in data['people'][1]:
    print(f"{second_inf} {data['people'][1][second_inf]}")