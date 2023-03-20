#Task 1: Dictionary, Set, Tuple
#1. Determine best data structure to efficiently store data for each scenerio
#2. Implement data structure 
    #1. Store monthos of the year as strings
        #a. Determine month in which National Pi Day is and print to console
            #access by index number
            #Ordered
            #Does not need to be changed

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(len(months))
print(months)
print(type(months))
print(months[0])
print(months[0:11])
print(months[:5])
print(months[5:])
print(months[-4:-1])

if 'Spring' in months:
    print("Yes, 'Spring' is a month")
else:
    print("No, 'Spring' is NOT a month, it is a season")

print(months[2])

#2. Store five fruits or vegetables
    #a. Add two favorite fruits and two favorite veggies to collection
    #b. Iterate over the collectiona and print each one to console
        #Unordered
        #Add elements
        #Do not need to access individual elements
        #Unique, no duplicates

produce = {'apple', 'pineapple', 'mango', 'cucumber', 'avocado'}
print(produce)
produce.add('tomato')
print(produce)
produce.update(['spinach', 'grapefruit', 'honeydew'])
print(produce)
produce.copy
print(produce)
produce.discard('tomato')
print(produce)
produce.pop
print(produce)

#3. Store user profile info
    #a. Literal string interpolation to print profile info to console
    #b. Profile Info to include:
        #1. First Name
        #2. Last Name
        #3. Email Address
        #4. Phone Number
            #Ordered
            #Items must be changeable
            #Must be able to access individual items
            #Items must be mutable

first_name = 'Bob'
last_name = 'Smith'
email_address= 'bobs@email.com'
phone = '555-777-9999'

print(f'User Profile: Full Name {first_name} {last_name} Contact Information {email_address} {phone}')
