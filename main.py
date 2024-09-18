#*Create a function* that takes an array, an index, and a value as parameters. 
# Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.

def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr



#*Implement a simple shopping cart program* using an array. 
# Create functions to add items, remove items, and update quantities using array methods. 
# Print the cart's contents after each operation.
def add_item(cart, item):
    cart.append(item)
    return cart
def remove_item(cart, item):
    cart.remove(item)
    return cart
def update_quantity(cart, item, quantity):
    cart[cart.index(item)] = quantity
    return cart

cart = []
cart = add_item(cart, "apple")
print(cart)
cart = add_item(cart, "banana")
print(cart)
cart = add_item(cart, "orange")
print(cart)
cart = remove_item(cart, "banana")
print(cart)
cart = update_quantity(cart, "apple", 5)
print(cart)


#*Write a program* that uses a while loop to print the first 25 integers.
i = 1
while i <= 25:
    print(i)
    i += 1

#*Write a program* that uses a while loop to print the first 10 even numbers.
i = 2
while i <= 20:
    print(i)
    i += 2

#*Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result    

#*Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        numbers.pop(i)
    else:
        i += 1
print(numbers)

#*Create a function* that takes an array of numbers as a parameter. 
# Use a while loop to calculate and return the sum of all the numbers in the array.
def sum_array(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

#*Implement a program* that takes a list of temperatures in Celsius as input from the user. 
# Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. 
# Use a while loop to perform the conversion for each temperature.
list_temp = input("Enter a list of temperatures in Celsius separated by commas: ")
list_temp = list_temp.split(",")

i = 0
while i < len(list_temp):
    list_temp[i] = float(list_temp[i]) * 9/5 + 32
    i += 1
print(list_temp)

#*Write a program* to remove all the odd numbers from an array.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
print(numbers)