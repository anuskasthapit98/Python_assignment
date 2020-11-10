#Assignment #1
#Exercise 1. Assume that we execute the following assignment statements:

width = 17
height = 12.0
delimiter = '.'

print('width/2-> value:{0} type{1}' .format((width/2) ,type(width/2)))
print('width/2.0> value:{0} type{1}' .format((width/2.0) ,type(width/2.0)))
print('height/3-> value:{0} type{1}' .format((height/3) ,type(height/3)))
print('1 + 2 * 5-> value:{0} type{1}' .format((1 + 2 * 5) ,type(1 + 2 * 5)))
print('delimiter * 5-> value:{0} type{1}' .format((delimiter * 5) ,type(delimiter * 5)))

# Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.

temp= int(input("Enter temperature in Fahrenhite: "))
celsius =(temp - 32)*5/9
print("Temperature in celsius: ",celsius)

# Exercise 3. Write a program that takes seconds as time units and converts it to minutes and seconds. 

time=int(input('Enter seconds: '))
minutes,second=divmod(time,60)
print(minutes ,':', second)

# Exercise 4. Consider a list of any arbitrary elements. Your code should print the length of the list and first and fourth element of the list.

words = ["Age", "Cabbage", "Cafe", "Gas","Apple","Cat","Mouse"]
print(len(words))
print(words[0],words[3])

# Exercise 5. Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove. 


words = [2, 1, 3, 5, 4, 3, 8]
words.pop(2)
print("After pop method ", words)
words.insert(1,16)
print("After insert method ", words)
words.remove(5)
print("After remove method ", words)




#Assignment #2
# Choose a list of your choice and find the sum of all elements of that list. 

sums=0
lists =  [2, 1, 3, 5, 4, 3, 8]
for item in lists:
    sums += item
print(sums)

# Write a program that returns a list which contains common elements from two lists. Avoid the duplicate elements from lists.

a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
c=[]
for item in a:
    if item in b and item not in c:
        c.append(item)
print(c)

# Suppose you have a list [1, 5, 7, 12 ,15] Print each number using loop. Also, print the square of each number using loop.

a =[1, 5, 7, 12 ,15]
for item in a:
    print(item)
    print(item**2)


# Write a code to ask an input from the user which is a string and display the string along with its length.

string = input("Enter a word: ")
print(string)
count = 0
for i in string:
    count = count + 1
print(count)


# Write a code to ask an input from the user which is a string and convert it to uppercase and lowercase


string = input("Enter a word: ")
print(string.upper())
print(string.lower())



#Assignment #3

# Write a program to display all prime numbers from 1 to 100.
for num in range (1, 101):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print(num, end = '  ')




# Ask the user for a string and print out whether this string is a palindrome or not.

string = input("enter a word: ")
if string[::-1] == string:
    print("This is a palindrome")
else:
    print("This is not a palindrome")



# Given a string, count all lower case, upper case, digits and special symbols.

low=0
up=0
digit=0
special = 0
string = input("enter a sentence: ")
for i in range(len(string)):
    if string[i].isupper():
        up = up+1
    elif string[i].islower():
        low = low+1
    elif string[i].isdigit(): 
        digit += 1
    else: 
        special += 1
print('Upper case letters:', up) 
print('Lower case letters:', low) 
print('Numbers:', digit) 
print('Special characters:', special) 



# Write a program to display the n terms of harmonic series and their sum. 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n 


n = int(input("enter a limit: "))
i = 1
s = 0.0
for i in range(1, n+1): 
    s = s + 1/i; 
print("Sum is", round(s,3)) 




#  Write a program to display the following pattern. Check also with different number of rows


rows = int(input("enter a number: "))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")



# Create a dictionary that has a key value pair of letters and the number of occurrences of that letter in a string.


dict= {}
string = 'pineapple'
for item in string:
    keys = dict.keys()
    if item not in keys:
        dict[item]=1
    else:
        dict[item] += 1

print(dict)
        

    
    
