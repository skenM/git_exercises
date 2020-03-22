string = "ABC ABC"
print (string)
words = 1
letters = 0
hash_table = {}

lista_string = string.split(" ")
print (lista_string)

for char in string:
    char = char.lower()
    if char  == ' ':
        words+=1
    else:
        letters+=1
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1


print ("Podany ciag znakow sklada sie z",words,"wyrazow.")
print ("Podany ciag znakow sklada sie z", letters, "znakow")
print ("Czestotliwosc wystepowania znakow:", hash_table)


