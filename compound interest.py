# program for a compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = int(input("Enter the principal amount: "))
    if principal <= 0:
        print("principal can't be less than or equal to zero.")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero.")

total = principal * pow((1+rate/100), time)
print(f"The total balance after {time} year/s is ₹{total:.2f}")

