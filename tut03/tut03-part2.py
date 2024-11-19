a=input("Enter Your String:")
permutations=list(a)
indices=[0]*len(a)
print("".join(permutations))
i=0
while i< len(a):
  if(indices[i]<i):
      if(i%2==0):
        permutations[0],permutations[i]=permutations[i],permutations[0]
      else:
        permutations[indices[i]],permutations[i]=permutations[i],permutations[indices[i]]
        indices[i]+=1
      print("".join(permutations))
      indices[i]+=1
      i=0
  else:
      indices[i]=0
      i+=1