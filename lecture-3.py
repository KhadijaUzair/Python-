a = "1"
b = "2"
print(a + b) #this is string which is why the output will be 12 and not 3

c= 1
d = 2
print (c + d) # this is interger and the output will be 3

# to convert string into integer we will write int()

print(int(a) + int(b)) # this will convert string to interger and then perform the operation and is called explicit typecasting

# implicit typecasting means which python is doing by itself for example 1 + 1.9 = 2.9 so python given us andswer in float 

# Taking user from input

#x = input()
#print("my name is ",x)

y = input("Enter your name: ")
print("My name is ",y)

r = input("Enter first number: ")
s = input("Enter second number: ")
print(int(r) + int(s)) #if we didnt write int then whatever number we write in the input will be written as it is in the output


