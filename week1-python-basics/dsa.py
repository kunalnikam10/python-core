
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

l1= [2,5,3,5,6,3,11,7,8,14,4,2]

print(second_largest(l1))
