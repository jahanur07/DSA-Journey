n=int(input("Enter the len of list"))
mylist=input().split(" ")

for i in range(n):
  mylist[i]=int(mylist[i])
  
print(mylist)