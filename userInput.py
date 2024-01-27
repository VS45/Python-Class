# Taking input from the keyboard
age=5
try:
    age=int(input("Age: "))
    print(age)
except ValueError as ve:
    print("Wrong value: ",ve)
name=input("Your Name: ")
print(name,",You are Welcome! Your age is ",age)