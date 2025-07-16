#find simple interest
p=float(input("enter first number:"))
r=float(input("enter second number:"))

y=int(input("enter year:"))
ci=p(1+r/100)**y
in=ci-p
print("interest:",in)
print("ci:",ci)
