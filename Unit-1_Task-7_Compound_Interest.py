p=float(input("enter principal amount:"))
r=float(input("enter rate of interest:"))
t=int(input("enter time in years:"))
amount=p*(1+r/100)**t
ci=amount-p
print("compound interest:",ci)
print("total amount:",amount)