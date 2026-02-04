a=9
b=23
a,b=b,a
# print(a,b)

num= 13.45333
# print(float(num))
# print(int(num))

def rev(s):
  reversed_str=""
  for i in s:
    reversed_str= i+reversed_str
  print(reversed_str)

# rev("Python Developer")

def vow(s):
  count=0
  vowels= "aeiouAEIOU"
  for i in s:
    if(i in vowels):
      count+=1
    
  print(count)

# vow("DataEngineering")

def palin(s):
  start =0
  end=len(s)-1
  for i in s:
    if(s[start]!=s[end]):
      return False
    else:
      start+=1
      end-=1
  return True

def palin2(s):
  s=s.lower()
  return s==s[::-1]

# print(palin2("Maam"))

def removedup(l):
  l2=[]
  for i in l:
    if i in l2:
      continue
    else:
      l2.append(i)

  return l2

l1=[1,2,2,3,4,4,5]

# ans=removedup(l1)
# print(ans)

def secondl(l):
  largest=l[0]
  slargest=-1

  for i in l:
    if i>largest:
      slargest=largest
      largest=i
    elif i>slargest:
      slargest=i
  return slargest

def evenodd(l):
  evenlist=[]
  oddlist=[]

  for i in l:
    if(i%2==0):
      evenlist.append(i)
    else:
      oddlist.append(i)
  print("Even list: ", evenlist)
  print("Odd list: ", oddlist)

numbers=[1,2,32,44,2,22,44,5,666,554,33,222,555]

# print(secondl(numbers))
# evenodd(numbers)

def runningsum(l):
  ans=[]
  sum=0

  for i in l:
    sum+= i
    ans.append(sum)

  print(ans)

newl=[1,2,3,4]
# runningsum(newl)

def char_frequency(s):
  freq={}

  for i in s:
    freq[i]= freq.get(i,0)+1

  return freq

s2="kunallldoodk"
print(char_frequency(s2))