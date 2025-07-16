#find compound interest
p=float(input("enter first number:"))
r=float(input("enter second number:"))
y=float(input("enter year:"))
ci=p*(1+r/100)**y
i=ci-p
print("interest:",i)
print("ci:",ci)
