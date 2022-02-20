import sys
f = open(sys.argv[1], "r")
nums = f.read().replace("\n", " ").split(" ")
f.close()
for i in range(len(nums)):
    nums[i] = int(nums[i])
sum=sum(nums)
len=len(nums)
sr= round(sum/len)
i=0
k=0
for i in range(len):
    while nums[i]!=sr:
        if nums[i] > sr:
            nums[i]-= 1
            #print(nums)
            k+=1
        elif nums[i] < sr:
            nums[i]+= 1
            #print(nums)
            k += 1
        else:
            i+=1
print(k)
f.close()






