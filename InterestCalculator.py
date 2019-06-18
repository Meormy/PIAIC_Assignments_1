# A = Total Accrued Amount (principal + interest)
# P = Principal Amount
# I = Interest Amount
# r = Rate of Interest per year in decimal; r = R/100
# R = Rate of Interest per year as a percent; R = r * 100
# t = Time Period involved in months or years
# Equation:
# A = P(1 + rt)

P = int(input("Enter Amount : "))
R = int(input("Enter Rate : "))
r = float(R / 100)
t = int(input("Enter Time Period : "))
A = P * (1 + (r*t))
print (A)
