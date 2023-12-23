a=input("chose an operator to do calc: \"+ - * /\": ")
b=int(input("Enter the number 1: "))
c=int(input("Enter the number 2: "))
if(a=="+"):
  n=b+c
elif(a=="-"):
  n=b-c
elif(a=="*"):
  n=b*c
elif(a=="/"):
  n=round((b/c),3)
print(n)