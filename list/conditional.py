#conditional statements
tobisAge = 23.9
amakasAge = 24

if tobisAge > amakasAge:
    print("Tobi is older than Amaka")
elif tobisAge == amakasAge:
    print("Tobi is Amaka's age mate")
else:
    print("Amaka is older than Tobi")



counter = 1

while counter < 20:
    print(counter)
    counter += 1

number = 20

while number > 1:
    print(number)
    number -= 1


counter = 0

while counter <= 25:
    print("Amaka: %s" %(counter))
    counter += 1



print("Amaka is a bad ass " + "programmer")

# For loop

for num in range(1,20):
    print(num)