
#while loops: runs continuosly as long as a certian condition remains true
prompt = ("\n Tell me something and i'll repeat it back to you")
prompt += "\nEnter 'Quit' to end the program. "

message = ""
while message != 'Quit':
    message = input(prompt)

    if message != 'Quit':
         print(message)
#using a flag
prompt = ("\n Tell me something and i'll repeat it back to you")
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#using break to  end a while loop
prompt = ("\nPlease tell me the names of the cities visited.")
prompt += "\nenter 'quit' to end the program. "

while True:
    cities = input(prompt)
    if cities =='quit':
        break
    else:
        print(f"I love {cities.title()}!")

#using continue in a while loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
