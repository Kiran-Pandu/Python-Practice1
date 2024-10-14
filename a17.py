# Given an integer n, perform the following conditional actions:
# • If n is odd, print WEIRD
# • If n is even and in the inclusive range of 2 to 5, print NOT
# WEIRD
# • If n is even and in the inclusive range of 2 to 5, print
# WEIRD
# • If n is even and greater than 20, print NOT WEIRD
# Note:
# Integer n must be a positive number, greater than 0
n = int (input("Enter The Integer Number : "))
if n<=0:
    print("Please Enter a Positive Integer")
elif n%2!=0:
    print("WEIRD")
elif n % 2 == 0:  
        if 2 <= n and n<= 5:
            print("NOT WEIRD")
        elif 6 <= n and n<= 20:
            print("WEIRD Less than 20")
        elif n > 20:
            print("NOT WEIRD")

