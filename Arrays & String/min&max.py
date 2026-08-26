n=int(input("Enter len of list :"))
mylist=input().split()

for i in range(n):
  mylist[i]=int(mylist[i])
  
  
minval=mylist[0]
maxval=mylist[0]

for val in mylist:
  if val<minval:
    minval=val
  if val>maxval:
    maxval=val
    
print(f"minval is {minval},maxval is {maxval}")


#inbuild methode
# maxelm=max(mylist)
# minelm=min(mylist)
# print(minelm,maxelm)