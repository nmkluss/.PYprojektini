#cikls ar skaitītāju
for number in range(5):
    print("Attempt", number+1, (number + 1) * ".")

for i in range(1,10, 2):
    print("Izmēģinājums", i)

successful = True
for x in range(3):
    print("Attempt")
    if successful:
        print("Successful!")
        break
else: #for else statement, else bloks kas izpildīsies pēc cikla izpildes
    print("Attempted", x+1 , "times and failed.")

#cikli ciklā
for a in range(4):
    for b in range(4):
        print(f"{a}, {b}")
#divi cikli, ārējais un iekšējais
#pirmais a=0 
#b=0, tad turpinu iekšējo ciklu b=1, b=2
#otrais a=1
#b=0, b=1, b=2

print(type(5))
print(type(range(2)))
#range objektu var izmantot kā skaitītāju 
#Iterable
for e in range(5):
    print(e)

for t in "Saraksts!":
    print(t)

for u in [1, 2, 3, 4, 5]:
    print(u)

#while cikls
number = 100
while(number > 0):
    print(number)
    number = number // 2 #vai //=

#command = ""
#while command.lower() != "quit":
#    command = input(">")
#    print("ECHO", command)
l = 0
for n in range(10):
    if n%2 == 0:
        print("Even!")
        l += 1
    else:
        print("Odd!")
print(f"We have {l} even numbers!")

