import random
c=-1
while(c!=0):
  list=[1,2,3]
  a=int(input("1-rock,2-paper,3-scissors: "))
  b=random.choice(list)
  print("Computer choice: "+str(b))
  if(a>0 and a<=3):
    if(a==b):
      print("draw")
    elif(a==1 and b==2):
      print("Computer wins")
    elif(a==2 and b==1):
      print("You wins")
    elif(a==1 and b==3):
      print("You wins")
    elif(a==3 and b==1):
      print("Computer wins")
    elif(a==2 and b==3):
      print("Computer wins")
    elif(a==3 and b==2):
      print("You wins")
    c=int(input("Enter : 0 - exit else other no. to retry"))
  else:
    print("Enter the valid number!!")
