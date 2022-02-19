nums = [1,2,3]
sr= round(sum(nums)/len(nums))
#print(int(sr))
k=0
for i in nums:
    if nums[i] > sr:
        nums[i] + 1
        k+=1
    elif nums[i] < sr:
        nums[i] + 1



