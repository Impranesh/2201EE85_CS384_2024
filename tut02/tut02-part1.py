a=input("Enter Your Number:")
b=int(a)

while b>10:
  sum=0
  while b>0:
    sum+=b%10
    b=b//10
  b=sum
print(b)