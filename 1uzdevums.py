text = input("Please input a word or sentence:")
#Length of the string.
garums = len(text)
print(f"The length of you text is {garums}")
#The string in all uppercase and all lowercase.
print(text.upper())
print(text.lower())
#The string reversed
reversed = text[::-1]
print(reversed)
#Count of each vowel (a, e, i, o, u) in the string
a = e = i = o = u = 0
for char in text.lower():
    if char == "a":
        a += 1
    elif char == "e":
        e += 1
    elif char == "i":
        i += 1
    elif char == "o":
        o += 1
    elif char == "u":
        u += 1
print(f"a: {a}, e: {e}, i: {i}, o: {o}, u:{u}")
#Whether the string is a palindrome
cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
if cleaned_text == cleaned_text[::-1]:
    print("Is Palindrome: Yes")
else:
    print("Is Palindrome: No")