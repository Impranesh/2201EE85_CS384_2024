# Part-01 Tutorial-02

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    primes_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return primes_numbers # return the list of prime numbers


sieve_of_eratosthenes(100000)



a=input("Enter Your Number:")
b=int(a)
ck=True
if(b not in sieve_of_eratosthenes(100000)):
  ck=False
for i in range(len(a)-1,0,-1):

  a=a[i:]+a[:i]
  if(int(a) not in sieve_of_eratosthenes(100000)):
    ck=False

if ck:
  print("Rotations are Prime.")
else:
  print("Rotations are not Prime.")


  # Part-02 Tutorial-02


  
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
