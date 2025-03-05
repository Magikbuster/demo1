# Practice Programs for Mathematical calculations with respect to variables
# 3. (A+B+C)^2 = A^2 + B^2 + C^2 + 2(AB+BC+CA)
A = 4
B = 2
C = 3
LHS = (A+B+C)**2
RHS = A**2 + B**2 + C**2 + 2*(A*B + B*C + C*A)
print("LHS: ", LHS)
print("RHS: ", RHS)

# 4. Area of circle: Area = PI*R^2 (PI = 3.13 & R = 5)
PI = 3.14
R = 5
Output_Area = PI*R**2
print(Output_Area)

# 5. Simple Interest Calculation
"""
si = (p+r+t)/100
p = principal amount
r = rate of interest
t = time
"""
p=1000
r=12
t=5
si=(p+r+t)/100
print("Simple Interest: ", si)

# 6. Compound Interest
"""
ci = ((p*(1+i)^n) - p)
p = principal amount
i = interest rate
n = time period
"""
p=1000
i=5
n=2
ci= ((p*(1+i)^n) - p)
ci1= ((p*(1+i)**n) - p)
ci2= (((1+i)**n*p) - p)
print("Compound Interest: ", ci)
print("Compound Interest: ", ci1)
print("Compound Interest: ", ci2)

print("done")