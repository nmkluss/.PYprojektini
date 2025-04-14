#simbolu virknes apstrāde
simboluVirkne = "Šī ir augsta līmeņa simbolu virkne programmēšanas valodā python."
print(simboluVirkne)
x = len(simboluVirkne)
print(x)
simboluVirkne2 = "Kaut kāda papildus informācija."
simboluVirkne3 = simboluVirkne + " " + simboluVirkne2 #pirmais variants kā savienot simbolu virknes.
simboluVirkne4 = f"{simboluVirkne} {simboluVirkne2}" #otrais variants kā savienot simbolu virknes
print(simboluVirkne3)
print(simboluVirkne4)
# .funkcijas sauc par metodēm. Programmēšanas valodā python visi elementi ir objekti kuriem ir funkcijas, kuras sauc par metodēm un tās var izmantot ar .
print(simboluVirkne.upper())
print(simboluVirkne.title())
print(simboluVirkne.find("ir")) # ar metodi find ir iespējams atrast meklējamā simbola vai simbolu virknes indeksu 
print(simboluVirkne.replace("a", "z"))
print("ir" in simboluVirkne) #atgriež būla vērtību vai simbolu virkne "ir" tiek atrasta simbolu virknē
print("nav" in simboluVirkne)



