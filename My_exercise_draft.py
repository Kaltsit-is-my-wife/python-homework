from decimal import Decimal,getcontext

getcontext().prec = 100
pi = Decimal("4")
print(pi)
n = int(input("please enter the times of calculating:"))
for i in range(n):
    pi += pi/(i*2 + 1)*((-1)*i)

print(pi)