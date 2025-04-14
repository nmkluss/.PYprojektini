vecums = 20 
if vecums >= 20:
    ziņojums = "Atļauts!"
else: 
    ziņojums = "Nav atļauts!"
#vai
#ziņojums = "Atļauts!" if vecums >= 20 else "Nav atļauts!"
print(ziņojums)


#loģiskie operatori 
#loģiskais un/ loģiskais vai/ noliegums
# & and, or, not 
augstiIenākumi = True
navParādsaistību = True
student = True
if (augstiIenākumi or navParādsaistību) and not student:
    print("Aizdevums pieejams!")
else:
    print("Aizdevums nav pieejams!")

#salīdzināšanas operatoru saistīšana
skaits = 30
if skaits >= 12 and skaits < 50: 
    print("Atlaide!")
#vai
# if 12 <= skaits < 50
