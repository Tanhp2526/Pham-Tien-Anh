import json

#du lieu ban dau
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address' : {
        "streetAddress" : "21 2nd Street",
        "city" : "New York",
        "state" : "NY",
        "postalCode" : "10021-3100",
    }
}

#ghi du lieu vao file json
with open("person.json", 'w') as f:
    json.dump(person, f) 

json_object = json.dumps(person, indent= 4)

with open("person.json", 'r') as file:
    data= json.load(file)

print(data)
