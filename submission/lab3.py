#Stundent name: Lintong Wu
#Student number: 040994127
#Section: 302

import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
country_code = str(input('Type country code here: ').upper()) #Make the input's type string.

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
counts = {}
for code in l: #Scan the list and find if the user's input matches the code in list.
    if code in counts:
        counts[code] += 1 #use if else so every time it finds a match the counter will add 1.
    else:
        counts[code] = 1

#Format and print the result
print(counts.get(country_code))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
population = 0
while True:#Use the condition in while loop to avoid the invalid input.
    try:
        population = int(input('Type population here: '))
    except ValueError:
        print('Please enter a valid integer')
        continue
    else:
        break

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
for index in range (0, len(l1)):
    if l1[index] > population: #Condition to check if the number in l1 is bigger the  user's input.
        lstOfRecords.append(index)

#Print the list l1
print(l1)

#Bonus: Print the name of the cities whose index is in l1
print(lstOfRecords)
