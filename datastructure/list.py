fruits = ["apple", "banana", "orange","pineaple"]
print(type(fruits)) # this will give the type of datastructure 
print(fruits)
print(len(fruits)) # number of elements in a list
fruits.reverse() # This is to reverse the order of list and it mutate the initia values
print(fruits)

for i in fruits:
    print(i)

numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in numbers:
    x=i*2
    print(x)

fruits = ["Mango","Cucumber","Pear","Apple", "Banana", "Orange","Pineaple"]
fruits.sort()
print(fruits)
numbers.append(13) # add an element to list
print(numbers)
number3Element=fruits[2] # slice the list to have the number 3 element 
print(number3Element)
secondNumbers=[20,30,40,50]
numbers.extend(secondNumbers)
print(numbers)

bringfireFamily=["Stephen","John","Theresa","Dorcas"]
bringfireFamily.insert(1,"Jacob")
print(bringfireFamily)
myStudents=["Jessica","Dooshima","Tom","Tormusa","Abigail","Kachi","Ahmed","Nguevese","Loveth","Gloria","Kelvin"]
print(len(myStudents))
myStudents.pop(10)
print(myStudents)
countNumber=myStudents.count("Kachi")
print(countNumber)