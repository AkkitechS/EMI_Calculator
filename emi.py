import datetime as dt


p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest in %:"))
n = float(input("Enter the time(in years):"))

r = r / (12 * 100)
n = n * 12
rpn = ((1 + r) ** n)

emi = (p * r * rpn) / (rpn - 1)

date = str(dt.datetime.now())
print(f"Your Monthly emi is {emi}")
print(date[:10] + "-" + date[11:19].replace(":", "-"))