## Intro to functions
def x(input):
    output = input + 3
    return output

y = x(10)
print(y)

def pay(hours):
    pay_a = hours * 15
    pay_b = pay_a * (1 - .12)
    return pay_b

payment = pay(40)
print(payment)

payment_b = pay(32)
print(payment_b)

## Functions with mugit statusltiple arguments
def pay(hours, wage, tax):
    pay_a = hours * wage
    pay_b = pay_a * (1 - tax)
    return pay_b

pay_x = pay(40, 24, .22)
print(pay_x)

pay_y = pay(40, 15, .12)
print(pay_y)

## Functions with no arguments
def fx():
    print("Hello, you!")
    print("Good morning!")
fx()

#Exercise 1
def xy(beds, baths):
    value = (beds * 30000) + (baths * 10000) + 80000
    return value
z = xy(2,1)
print(z)

o1 = xy(2,3)
o2 = xy(3,2)
o3 = xy(3,3)
o4 = xy(3,4)

print(o1)
print(o2)
print(o3)
print(o4)

#Exercise 2
import math

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total = sqft_walls + sqft_ceiling
    gallon = total / sqft_per_gallon
    cost = gallon * cost_per_gallon
    return cost
project_cost = get_cost(432,144,400,15)
print(project_cost)

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total = sqft_walls + sqft_ceiling
    gallon_a = total / sqft_per_gallon
    gallon_b = math.ceil(gallon_a)
    cost = cost_per_gallon * gallon_b
    return cost
get_actual_cost(432, 144, 400, 15) 
print(get_actual_cost)
