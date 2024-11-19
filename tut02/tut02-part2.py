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