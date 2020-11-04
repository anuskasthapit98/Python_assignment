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




