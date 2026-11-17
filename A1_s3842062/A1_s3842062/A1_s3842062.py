#Ethan Haberl - s3842062
#Exercise 1

integer = 42
flt = 4.2
string = "hello"

print("My integer is:", integer)
print ("My float is:", flt)
print("My string is:", string)
print("The division is", integer/flt)


#Exercise 2

try:
    height = float(input("What is your height (m)? "))
    weight = float(input("What is your weight (kg)? "))
    BMI = 0.0
    BMI = weight / height**2

    print("Your BMI is:", BMI)
    if(BMI <= 20):
        print("Your BMI is considered underweight.")
    elif(BMI <= 25):
        print("Your BMI is considered standard.")
    else:
        print("Your BMI is considered overweight.")
except:
    print("You should have entered float/integer.")


#Exercise 3

upper_bound = int(input("What is the upper bound (int)? "))
divisor = int(input("What is the divisor (int)? "))

print(divisor, "is a divisor for:")
x = 1
while(x <= upper_bound):
    if(x % divisor == 0):
        print(x, end=(" "))
    x = x + 1
print("")

print(divisor, "is not a divisor for:")
y = 1
while(y <= upper_bound):
    if (y % divisor != 0):
        print(y, end=(" "))
    y = y + 1
print("")
