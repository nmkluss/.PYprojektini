#Single line comment 
print("Hello, world!") #the print() function is used to display any object to the screen, this object will be converted into a string before output.
input("Write your name!") #input(promt), a promt is the default message before the input
#x = input("Write your age!") #the input is saved in a variable x 
#print("You were this old last year: ", x-1) this will not work because the received input is a string, which means we have to convert it 
x = input("Write you age!")
x = int(x)
print("You were this old last year:", x-1)
#Python data types 
#text types - str, numeric types - int, float, complex, sequence types - list(ka masivs c++), tuple, range
#mapping types - dict, set types - set, frozenset, boolean types - bool,binary types - bytes, bytearray, memoryview, none types - nonetype
print(type(x)) #lai noskaidrotu mainīgā datu tipu ir jāizmanto funckija type()


                     