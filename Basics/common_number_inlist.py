# # brout force solution
# n=[2,1,3,1,2,3,1,5,5,4,5,4]
# m=[1,3,1,4,5]



# for i in m:
#   count = 0
#   for x in n:
#     if i==x:
#       count+=1
#   print(f"{i} in this array {count}")

#optimum solution

n=[2,1,3,1,2,3,1,5,5,4,5,4,4,4,4,4,4,4,4,4,]
m=[1,3,1,4,5]

hash_list=[0]*6

for i in n:
  hash_list[i]+=1
  

for num in m:
  if num<0 or num>6:
    print(0)
  else:
    print(hash_list[num])