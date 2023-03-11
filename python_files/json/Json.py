from json import loads as lds
from json import dumps as dmps

people_inf = '''
{
    "people": [
        {
            "name": "Ali Barkhordar",
            "phone": "09121209120",
            "email": ["ali.barkhordar@gmail.com", "a.barkhordar@gmail.com"],
            "registered": false
        },
        {
            "name": "Alireza Barkhordar",
            "phone": "09111209110",
            "email": ["areza.barkhordar@gmail.com", "ar.barkhordar@gmail.com"],
            "registered": true
        }
        ]
}
'''
# data is dict formatted of the json:people_inf
data = lds(people_inf)
# data2 turned poeple_inf back to json
data2 = dmps(people_inf)
# indent makes it more readable with spaces
data3 = dmps(people_inf, indent=4)
# sorts alfabetically (a-z)
data4 = dmps(people_inf, indent=4, sort_keys=True)

print(type(data))
print(type(data['people']))
print(type(data['people'][0]))
print(type(data['people'][1]))
print(type(data['people'][0]['email']))
print(type(data['people'][1]['registered']))

print(data)

print(data2)
print(type(data2))

print(data3)
print(data4)