## Integers
# Integers are numbers without any fractional part and can be positive (1, 2, 3, ...), negative (-1, -2, -3, ...), or zero (0).
x = 14
print(x)
print(type(x))

## Floats
# Floats are numbers with fractional parts.
phi = 3.141592653589793238462643383279502884197169399375105820974944
print(phi)
print(type(phi))

phi_2 = 22/7
print(phi_2)
print(type(phi_2))

rounded_phi = round(phi_2, 2)
print(rounded_phi)
print(type(rounded_phi))

float_a = 2.
print(float_a)
print(type(float_a))

## Booleans¶
# Booleans represent one of two values: True or False.
z = True
print(z)
print(type(z))

y = False
print (y)
print(type(y))

xy = (1>2)
print(xy)
print(type(xy))

yz = not xy
print(yz)
print(type(yz))

## Strings¶
# The string data type is a collection of characters (like alphabet letters, punctuation, numerical digits, or symbols) contained in quotation marks. 
w = "Hello World!"
print (w)
print(type(w))
print(len(w))

wx = ""
print(type(wx))
print(len(wx))

n = "1.12321"
print (n)
print(type(n))
print(len(n))

nx = float(n)
print (nx)
print(type(nx))

ny = "abc" + "def"
print(ny)
print(type(ny))

nz = "abc" * 4
print(nz)
print(type(nz))

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

# Exercise 1
def xyz(beds, baths, has_basement):
    value = (beds * 30000) + (baths * 10000) + (has_basement * 40000) + 80000
    return value
xyz(1, 1, 0)

# Exercise 2
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10*len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost
project_one = cost_of_project("Charlie+Denver", True)
print(project_one)
project_two = cost_of_project("08/10/2000", False)
print(project_two)
