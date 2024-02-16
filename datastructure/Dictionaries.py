# Dictionaries
person = {"name": "Alice", "age": 30, "city": "Makurdi"}
myName=person["name"]

# Access and modify dictionary values
print("Name:", myName)

mobile={"brand":"Tecno","model":"s10","price":509}
print(mobile)
print(mobile.values())
print(mobile.keys())

for x,y in mobile.items():
    print(x,y)
for i in mobile.values():
    print(i)
#check if a key exist in a dictionary
myKey=input("Enter Key: ")
if myKey in mobile:
    print(myKey," key exist in Mobile Dictionary!")
else:
    print("Key {} is not found in mobile Dictionary!".format(myKey))