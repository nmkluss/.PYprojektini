#Funkcijas
def sveiciens(vārds, uzvārds):
    print(f"Hi {vārds}, {uzvārds}!")
#funkcijas noklusējuma atgriežamā vērtība ir none

print(sveiciens("Allan", "Barry"))

def saņemt_sveicienu(vārds):
    return f"Hi {vārds}"

message = saņemt_sveicienu("Mark")
print(message)
file = open("content.txt", "w")
file.write(message)

def increment(number, by=2): #uzstādu noklusējuma vērtību, padarot parametrus neobligātus, visiem obligātajiem parametriem jābūt pirms izvēles
    return number + by

#answer = increment(10, 1)
#print(answer) vai 

print(increment(10, by=1)) #funkciju izsaukumus var padarīt lasāmākus ar atslēgas vārdu argumentiem
print(increment(10))


def reizinajums(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
print(reizinajums(1,2,3))