# Part-1 Tutorial-01

a=input("Enter Your Number:")
b=int(a)

while b>10:
  sum=0
  while b>0:
    sum+=b%10
    b=b//10
  b=sum
print(b)


# Part-2 Tutorial-02

a=input("Enter Your Input String ")
curr=0
b=""
for i in range( len(a)-1):
  if(a[i]==a[i+1]):
    curr+=1
  else:
    b+=a[i]
    b+=str(curr+1)
    curr=0

b+=a[len(a)-1]
b+=str(curr+1)
print(b)