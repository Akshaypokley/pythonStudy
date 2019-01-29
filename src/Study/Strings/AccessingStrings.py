#Python does not support a character type, these are treated as strings of length one, also considered as substring.
var1="Hi India!"
print(var1)
print (var1[1]) #Slice- it gives the letter from the given index
print("var1[2:3]",var1[1:6])#Range slice-it gives the characters from the given range

print("k" in var1) #Membership-returns true if a letter exist in the given string	u is present in word Guru and hence it will give 1 (True)

print("ld" not in var1) #Membership-returns true if a letter exist is not in the given string	l not present in word Guru and hence it will give 1

print('%s' % (var1))
name = 'guru'
number = 99
print('%s %d' % (name,number))#% - Used for string format	%r - It insert the canonical string representation of the object (i.e., repr(o)) %s- It insert the presentation string representation of the object (i.e., str(o)) %d- it will format a number for display

print(var1+str(number))#It concatenates 2 strings
print (var1*3) #It prints the character twice.