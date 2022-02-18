print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.division with remainders")
print("6.exponents and powers")
 
choice = int(input("> "))
 
a = float(input("enter your first number"))
b = float(input("enter your first number"))
 
if choice == 1:
    sum = a + b
    print("{} + {} + {}".format (a,b,sum))
 
elif choice == 2:
    difference = a - b
    print("{} - {} - {}".format (a,b,difference))
 
elif choice == 3:
    product = a * b
    print("{} * {} * {}".format (a,b,product))
 
elif choice == 4:
    quotient = a / b
    print("{} / {} / {}".format (a,b,quotient))
 
elif choice == 5:
    remainders = a / b
    print("{} / {} / {}".format (a,b,remainders))
 
elif choice == 6:
    exponents = a**b
    print("{} * {} * {}".format (a,b,exponents))
