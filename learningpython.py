# Task: Predict the output
a = 42
b = 3.14
c = "hello"
d = [1, 2, 3]
e = (4, 5, 6)
f = {"key1": "value1", "key2": "value2"}
g = {7, 8, 9}

# Try these operations and predict the results:
print(a + b)  # What happens?
print(c * 2)  # Guess the output!
print(d[1])   # Access second element
print(e[-1])  # Access last element
print("key1" in f)  # True or False?
print(len(g))  # Size of the set

# if else logic
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# for loop, iterate over a sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop, execute whilst a condition is true
count = 0
while count < 3:
    print(count)
    count += 1

# break and continue - control the loop flow
for num in range(5):
    if num == 5:
        break  # Exit loop
    if num == 2:
        continue  # Skip to the next iteration
    print(num)

# TASK
#Iterate through numbers 1 to 20.
#If the number is divisible by 3, print "Fizz".
#If the number is divisible by 5, print "Buzz".
#If the number is divisible by both 3 and 5, print "FizzBuzz".
#Otherwise, print the number itself.

for num in range(20): 
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: print(num)

# FUNCTIONS

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Arguments

def greet(name, greeting="Helloooo"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", greeting="Hi"))  # Output: Hi, Bob!

# Using functions with loops
def square(num):
    return num ** 2

for i in range(1, 6):
    print(square(i))  # Outputs: 1, 4, 9, 16, 25

# EXERCISE

#Write a function named fizzbuzz that:
#Accepts a single argument n.
#Loops through numbers 1 to n (inclusive).
#Prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both. Otherwise, it prints the number.
#Call your function for n = 20 to verify it works.

def calculate(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: return num
for i in range(1,21):
    print(calculate(i))


