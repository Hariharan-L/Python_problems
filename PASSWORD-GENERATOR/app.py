import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
special = "`~!@#$%^&*()_-+=/<>?:{\}[].,'|\""
tot=upper+lower+num+special
leng=int(input("Enter the length of the password you need: "))
password = "".join(random.sample(tot,leng))
print(password)