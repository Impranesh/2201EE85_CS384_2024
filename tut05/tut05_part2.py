a=input("Enter Your String:")
stack=[]
for i in range(len(a)):
  if(a[i]=="(" or a[i]=="[" or a[i]=="{"):
    stack.append(a[i])
  else:
    if(len(stack)==0):
      print("The input string is not balanced.")
      break

    else:
        if(a[i]==")" and stack[-1]=="(" or a[i]=="]" and stack[-1]=="[" or a[i]=="}" and stack[-1]=="{"):
          stack.pop()
        else:
          print("The input string is not balanced.")
          break
if(len(stack)==0):
  print("The input string is balanced.")