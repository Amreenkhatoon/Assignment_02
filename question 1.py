ascii_dict = {}

#for loop to iterate through the alphabet a to z
for letter in range(ord('a'),ord('z')+1):
    
    #convert the ascii value
    ascii_dict[chr(letter)]=letter

#print the dict
print(ascii_dict)