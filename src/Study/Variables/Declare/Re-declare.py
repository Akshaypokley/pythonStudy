a=12 # Declare a variable and initialize i
print (a)

# re-declaring the variable works
a = 'guru99'
print (a)

#Concatenate Variable
print("Concatenate Variable")

a=100
s="akshay"
print(str(a)+s) #Once the integer is declared as string, it can concatenate in the output.

#Local & Global Variables declaration

print("*****Local & Global Variables declaration*****")

a=56 #Global variable Declare
print (a)
def LocaVariableFun():
    a="I am local variable " # a is loacal variable declare inside the faction
    print(a)
LocaVariableFun()

# print the global variable using global keyword

b=100;
print (b)

def globalKeyFun():
    global b
print (b)
b="I am global Keyword"
print("Changing global variable "+" -->"+b)

print("@@@@@@@@@@@@@@@@@@@@@@@@")

c=100;
print (c)
print("Delete the variable ")
del c
print (c)

