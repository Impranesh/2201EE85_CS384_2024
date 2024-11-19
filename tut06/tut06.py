import os

def checkfile():
    if os.path.exists("input.txt"):
        return True
    else:
        return False


def fileOperation(a):
  with open ("input.txt",a[0]) as file:
    if(a[0]=="r"):
      return file.read()
    elif(a[0]=="w"):
      file.write(a[1]+"\n")
    elif(a[0]=="a"):
      file.write(a[1]+"\n")


def check(a, b):
  if(len(a)<8):
    return "Your Password must cosists of 8 characters and should be combination of uppercase,lowercase,(0-9),and (!,#,@)"
  special_chars="#@!"
  extra_char=""
  flags=[False]*4
  for i in range(len(a)):
    if(a[i].isupper() and 1 in b):
      flags[0]=True
    elif(a[i].islower() and 2 in b):
      flags[1]=True
    elif(a[i].isdigit() and 3 in b):
      flags[2]=True
    elif(a[i] in special_chars and 4 in b):
      flags[3]=True
    else :
        extra_char+=a[i]
  if(False not in [flags[int (x-1)] for x in  b ] and len(extra_char)==0):
    return True
  else:
      print("Invalid Password:")
      if not flags[0] and 1 in b: # Check for uppercase only if required
        print("Missing Uppercase")
      if not flags[1] and 2 in b: # Check for lowercase only if required
        print("Missing Lowercase")
      if not flags[2] and 3 in b: # Check for digits only if required
        print("Missing Digits")
      if not flags[3] and 4 in b: # Check for symbols only if required
        print("Missing Symbols")
      if(len(extra_char)!=0):
        print("These characters can't be used in password: ",extra_char)
      return False

ck=True
while(ck):
  b=input("Enter Your Password criterion 1-UpperCase, 2-LowerCase, 3-Numbers, 4-Special Character space seprated that you want:")
  b=[int(x) for x in b.split()]
  a=input("Enter Your Password it must consists of the uppercase,lowercase,(0-9),and special char(!, @, #):")
  if(check(a,b)==True):
    # print("Your Password is valid.")
    if(checkfile() and a+":Valid" in fileOperation(["r",a])):
      print("This Password is already exists.Try different one!")
    else:
      if(checkfile()):
        fileOperation(["a",a+":Valid"])
      else:
        fileOperation(["w",a+":Valid"])
      ck=False
      break
  else :
    if(checkfile() and a+":Invalid" not in fileOperation(["r",a])):
      if(checkfile()):
          fileOperation(["a",a+":Invalid"])
      else:
          fileOperation(["w",a+":Invalid"])