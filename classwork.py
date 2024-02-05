numb1=0
numb2=1
try:
    numb1=int(input("enter your first number: "))
    numb2=int(input("enter your second number: "))
except ValueError as ve:
    print("Wrong value: ",ve)
product=numb1*numb2
print(product)
