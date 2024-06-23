## Hello Python!

# Variable assignment
spam_amount = 0
print(spam_amount)

# Function calls
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# Numbers and arithmetic in Python
spam_amount = 0
type(spam_amount)
type(19.95)

print(5 / 2)
print(6 / 2)

print(5 // 2)
print(6 // 2)

# Order of operations
a = 8 - 3 + 2
print(a)
b = -3 + 4 * 2
print(b)

hat_height_cm = 25
my_height_cm = 190
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Builtin functions for working with numbers
print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
print(int('807') + 1)

#Exercise 1
color = "blue"
print(color)

#Exercise 2
pi = 3.14159 
diameter = 3

radius = diameter/2
print(radius)

area = pi * (diameter/2)**2
print(area)

#Exercise 3
a = [1, 2, 3]
b = [3, 2, 1]

tmp = a
a = b
b = tmp

#Exercise 4
alice_candies = 121
bob_candies = 77
carol_candies = 109

to_smash = (alice_candies+bob_candies+carol_candies)%3
print(to_smash)