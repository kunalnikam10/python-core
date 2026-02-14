from typing import List

def second_largest(l):
  largest= l[0]
  s_largest= -1

  for i in l:
    if(i> largest):
      s_largest = largest
      largest = i

    elif(i> s_largest and i< largest):
      s_largest = i

  return s_largest

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in nums:
            if(val != i):
                nums[k]= i
                k+=1

        return k
    
nums= [3,2,2,3]
sol =Solution()
print(sol.removeElement(nums, 3))
  

l1= [2,5,3,5,6,3,11,7,8,14,4,2]



# print(second_largest(l1))
