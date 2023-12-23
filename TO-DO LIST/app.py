list=[]
def addtask():
  a=input("Enter your task: ")
  list.append(a)
  print("your task is added.")
  print("For add more task: Enter 1 else Enter any other no. to exit")
  b=int(input())
  if(b==1):
    addtask()
def deltask():
  tot=len(list)
  p=int(input("Enter the number to be deleted: "))
  if(p>tot):
    print("number exceeding, enter a valid number")
    deltask()
  else:
    list.remove(list[p-1])
    print("AFTER REMOVING: ")
    viewtask()
def viewtask():
  print("########your task########")
  le=len(list)
  if (le!=0):
    t=1
    for i in list:
      print(str(t)+"."+str(i))
      t=t+1
choice=0
while(choice!=4):
  print("**********TO-DO LIST**********")
  print("1.Add your task")
  print("2.Delete your task")
  print("3.View your task")
  print("4.Exit")
  choice=int(input("Enter the number: "))
  if(choice==1):
    addtask()
  elif(choice==2):
    deltask()
  elif(choice==3):
    viewtask()
  elif(choice==4):
    print("Thanks for your response in the to do applications")
    break
  else:
    print("invalid number")