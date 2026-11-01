#method 1
nums=[2,3,1,6,8,3,4,9,4,4,4,3,1,2,1,3,3]
fre_map={}
for i in range(0,len(nums)):
  if nums[i] in fre_map:
    fre_map[nums[i]]+=1
  else:
    fre_map[nums[i]]=1
    
print(fre_map)