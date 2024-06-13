## Conditions
print(2 > 3)

a = 1
b = 2
print(a<1)
print(b>=2)

print(a==1)	#equals
print(a!=2)	#does not equal
print(a<2)	#less than
print(a<=1)	#less than or equal to
print(a>0)	#greater than
print(a>=1)	#greater than or equal to

## Conditional statements
# "if" statements
def evaluate_temp(temp):
    message = "Normal temperature."
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(37))
print(evaluate_temp(39))

# "if ... else" statements
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message
print(evaluate_temp_with_else(37))
print(evaluate_temp_with_else(39))

# "if ... elif ... else" statements
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
evaluate_temp_with_elif(36)
evaluate_temp_with_elif(34)

# Calculations
def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed
ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)

# Multiple "elif" statements
def get_dose(weight):
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    else:
        dose = 10
    return dose
print(get_dose(12))

#Exercise 1
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
get_grade(78)

#Exercise 2
def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10*len(engraving)
    else:
        cost = 50 + 7*len(engraving)
    return cost
cost_of_project("hello world", True)

#Exercise 3
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = num_gallons / 1000 * 5
    elif num_gallons <= 22000:
        bill = num_gallons / 1000 * 6
    elif num_gallons <= 30000:
        bill = num_gallons / 1000 * 7
    else:
        bill = num_gallons / 1000 * 10
    return bill
get_water_bill(25000)

#Exercise 4
def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + (gb - 15) * 100
    return bill
get_phone_bill(15.1)
get_phone_bill(15)
